internal static class AsmdefGraphResolver
{
    public static ResolvedProjectModel Resolve(UnityProjectModel project)
    {
        var asmdefsByName = project.AssemblyDefinitions.ToDictionary(item => item.Name, StringComparer.Ordinal);
        var guidToAssemblyName = project.AssemblyDefinitions
            .Where(item => !string.IsNullOrWhiteSpace(item.Guid))
            .ToDictionary(item => item.Guid, item => item.Name, StringComparer.OrdinalIgnoreCase);

        var assemblyContexts = new Dictionary<string, AssemblyContext>(StringComparer.Ordinal);
        foreach (var asmdef in project.AssemblyDefinitions)
        {
            assemblyContexts[asmdef.Name] = BuildAssemblyContext(project, asmdef, guidToAssemblyName);
        }

        var assemblyByFile = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        foreach (var file in project.SourceFiles)
        {
            var assemblyName = ResolveAssemblyForFile(project, file, asmdefsByName, guidToAssemblyName);
            assemblyByFile[file] = assemblyName;
        }
        AddMissingAssemblyContexts(project, assemblyContexts, assemblyByFile.Values);

        return new ResolvedProjectModel(project, assemblyContexts, assemblyByFile);
    }

    private static void AddMissingAssemblyContexts(
        UnityProjectModel project,
        IDictionary<string, AssemblyContext> assemblyContexts,
        IEnumerable<string> assemblyNames)
    {
        foreach (var assemblyName in assemblyNames.Distinct(StringComparer.Ordinal))
        {
            if (assemblyContexts.ContainsKey(assemblyName))
            {
                continue;
            }
            assemblyContexts[assemblyName] = AssemblyContext.Default() with
            {
                Name = assemblyName,
                Directory = project.ProjectDir,
            };
        }
    }

    private static AssemblyContext BuildAssemblyContext(
        UnityProjectModel project,
        AssemblyDefinition asmdef,
        IReadOnlyDictionary<string, string> guidToAssemblyName)
    {
        var diagnostics = new List<DiagnosticContract>();
        var completeness = AnalysisCompleteness.Complete;
        if (asmdef.Metadata.IncludePlatforms.Count > 0 && asmdef.Metadata.ExcludePlatforms.Count > 0)
        {
            diagnostics.Add(DiagnosticPolicy.PlatformConflict(asmdef.Name));
        }

        var references = asmdef.RawReferences
            .Select(reference => ResolveReference(reference, guidToAssemblyName, diagnostics, asmdef.Name, ref completeness))
            .Where(reference => !string.IsNullOrWhiteSpace(reference))
            .Distinct(StringComparer.Ordinal)
            .OrderBy(reference => reference, StringComparer.Ordinal)
            .ToArray();

        var effectiveDefines = new HashSet<string>(StringComparer.Ordinal);
        foreach (var symbol in BuiltInDefineSymbols(project.ProjectVersion))
        {
            effectiveDefines.Add(symbol);
        }
        if (project.Options.HasExplicitDefineSymbols)
        {
            foreach (var symbol in project.Options.ExplicitDefineSymbols)
            {
                effectiveDefines.Add(symbol);
            }
        }

        foreach (var versionDefine in asmdef.Metadata.VersionDefines)
        {
            if (!TryResolveVersionDefine(project, versionDefine, asmdef.Name, diagnostics, effectiveDefines, ref completeness))
            {
                completeness = AnalysisCompleteness.Partial;
            }
        }

        var includeInCompilation = EvaluateDefineConstraints(
            asmdef.Name,
            asmdef.Metadata.DefineConstraints,
            project.ProjectVersion is not null || project.Options.HasExplicitDefineSymbols,
            effectiveDefines,
            diagnostics,
            ref completeness);

        if (asmdef.Metadata.NoEngineReferences)
        {
            diagnostics.Add(DiagnosticPolicy.NoEngineReferencesRecorded(asmdef.Name));
        }
        if (!asmdef.Metadata.AutoReferenced)
        {
            diagnostics.Add(DiagnosticPolicy.AutoReferencedRecorded(asmdef.Name));
        }
        if (asmdef.Metadata.AllowUnsafeCode)
        {
            diagnostics.Add(DiagnosticPolicy.AllowUnsafeCodeApplied(asmdef.Name));
        }

        return new AssemblyContext(
            asmdef.Name,
            asmdef.RootNamespace,
            references,
            asmdef.Metadata,
            asmdef.Directory,
            diagnostics,
            completeness,
            effectiveDefines,
            includeInCompilation,
            []);
    }

    private static string ResolveAssemblyForFile(
        UnityProjectModel project,
        string sourceFile,
        IReadOnlyDictionary<string, AssemblyDefinition> asmdefsByName,
        IReadOnlyDictionary<string, string> guidToAssemblyName)
    {
        var sourceDirectory = Path.GetDirectoryName(Path.GetFullPath(sourceFile)) ?? project.ProjectDir;
        var asmref = project.AssemblyReferences.FirstOrDefault(item => UnityPaths.IsSameOrChild(sourceDirectory, item.Directory));
        if (asmref is not null)
        {
            var resolved = ResolveAsmrefReference(asmref.Reference, guidToAssemblyName);
            if (resolved is not null)
            {
                return resolved;
            }
        }

        var asmdef = project.AssemblyDefinitions.FirstOrDefault(item => UnityPaths.IsSameOrChild(sourceDirectory, item.Directory));
        return asmdef?.Name ?? AssemblyContext.Default().Name;
    }

    private static string ResolveReference(
        string reference,
        IReadOnlyDictionary<string, string> guidToAssemblyName,
        List<DiagnosticContract> diagnostics,
        string assemblyName,
        ref string completeness)
    {
        var trimmed = reference.Trim();
        const string guidPrefix = "GUID:";
        if (!trimmed.StartsWith(guidPrefix, StringComparison.OrdinalIgnoreCase))
        {
            return trimmed;
        }

        var guid = trimmed[guidPrefix.Length..].Trim();
        if (guidToAssemblyName.TryGetValue(guid, out var assemblyReference))
        {
            return assemblyReference;
        }

        diagnostics.Add(DiagnosticPolicy.UnresolvedAsmdefGuidReference(assemblyName, $"{guidPrefix}{guid}"));
        completeness = AnalysisCompleteness.Partial;
        return $"{guidPrefix}{guid}";
    }

    private static string? ResolveAsmrefReference(string reference, IReadOnlyDictionary<string, string> guidToAssemblyName)
    {
        const string guidPrefix = "GUID:";
        if (!reference.StartsWith(guidPrefix, StringComparison.OrdinalIgnoreCase))
        {
            return reference.Trim();
        }
        var guid = reference[guidPrefix.Length..].Trim();
        return guidToAssemblyName.TryGetValue(guid, out var assemblyName) ? assemblyName : null;
    }

    private static bool EvaluateDefineConstraints(
        string assemblyName,
        IReadOnlyList<string> constraints,
        bool hasExplicitDefineSymbols,
        IReadOnlySet<string> effectiveDefines,
        List<DiagnosticContract> diagnostics,
        ref string completeness)
    {
        if (constraints.Count == 0)
        {
            return true;
        }
        if (!hasExplicitDefineSymbols)
        {
            diagnostics.Add(DiagnosticPolicy.DefineConstraintsNotEvaluated(assemblyName));
            completeness = AnalysisCompleteness.Partial;
            return true;
        }

        foreach (var constraint in constraints)
        {
            if (!ConstraintMatches(constraint, effectiveDefines))
            {
                diagnostics.Add(DiagnosticPolicy.DefineConstraintsUnsatisfied(assemblyName));
                return false;
            }
        }
        return true;
    }

    private static bool ConstraintMatches(string expression, IReadOnlySet<string> defines)
    {
        var orParts = expression.Split("||", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
        foreach (var part in orParts)
        {
            var token = part.Trim();
            var negated = token.StartsWith('!');
            var symbol = negated ? token[1..].Trim() : token;
            var present = defines.Contains(symbol);
            if (negated ? !present : present)
            {
                return true;
            }
        }
        return false;
    }

    private static IEnumerable<string> BuiltInDefineSymbols(string? projectVersion)
    {
        if (string.IsNullOrWhiteSpace(projectVersion))
        {
            yield break;
        }
        var match = System.Text.RegularExpressions.Regex.Match(projectVersion, @"^(?<major>\d+)\.(?<minor>\d+)");
        if (!match.Success)
        {
            yield break;
        }
        var major = int.Parse(match.Groups["major"].Value, System.Globalization.CultureInfo.InvariantCulture);
        var minor = int.Parse(match.Groups["minor"].Value, System.Globalization.CultureInfo.InvariantCulture);
        yield return $"UNITY_{major}_{minor}_OR_NEWER";
    }

    private static bool TryResolveVersionDefine(
        UnityProjectModel project,
        VersionDefineContract versionDefine,
        string assemblyName,
        List<DiagnosticContract> diagnostics,
        ISet<string> effectiveDefines,
        ref string completeness)
    {
        var resourceVersion = ResolveResourceVersion(project, versionDefine.Name);
        if (resourceVersion is null)
        {
            diagnostics.Add(DiagnosticPolicy.VersionDefinesNotEvaluated(assemblyName));
            completeness = AnalysisCompleteness.Partial;
            return false;
        }

        if (!VersionExpressions.TryEvaluate(versionDefine.Expression, resourceVersion, out var matches))
        {
            diagnostics.Add(DiagnosticPolicy.InvalidVersionDefineExpression(assemblyName, versionDefine.Expression));
            completeness = AnalysisCompleteness.Partial;
            return false;
        }

        if (matches && !string.IsNullOrWhiteSpace(versionDefine.Define))
        {
            effectiveDefines.Add(versionDefine.Define);
        }
        return true;
    }

    private static string? ResolveResourceVersion(UnityProjectModel project, string resourceName)
    {
        if (string.Equals(resourceName, "Unity", StringComparison.OrdinalIgnoreCase))
        {
            return project.ProjectVersion;
        }
        return project.PackageVersions.TryGetValue(resourceName, out var version) ? version : null;
    }
}
