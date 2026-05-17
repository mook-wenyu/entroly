using Microsoft.CodeAnalysis;

internal static class ReferenceResolver
{
    public static ResolvedProjectModel AttachMetadataReferences(ResolvedProjectModel model)
    {
        var updated = new Dictionary<string, AssemblyContext>(StringComparer.Ordinal);
        foreach (var (name, context) in model.AssembliesByName)
        {
            updated[name] = context with
            {
                MetadataReferences = BuildMetadataReferences(model, context, out var diagnostics, out var completeness),
                Diagnostics = context.Diagnostics.Concat(diagnostics).ToArray(),
                AnalysisCompleteness = AnalysisCompleteness.Combine([context.AnalysisCompleteness, completeness]),
            };
        }
        return model with { AssembliesByName = updated };
    }

    private static IReadOnlyList<PortableExecutableReference> BuildMetadataReferences(
        ResolvedProjectModel model,
        AssemblyContext context,
        out IReadOnlyList<DiagnosticContract> diagnostics,
        out string completeness)
    {
        var contracts = new List<DiagnosticContract>();
        completeness = AnalysisCompleteness.Complete;
        var references = BasicReferences().ToList();

        var needsUnityEngine = !context.Metadata.NoEngineReferences && AssemblyNeedsUnityManagedMetadata(model, context);
        if (needsUnityEngine)
        {
            if (string.IsNullOrWhiteSpace(model.Project.Options.UnityManagedDir))
            {
                contracts.Add(DiagnosticPolicy.UnityManagedReferencesMissing(context.Name));
                completeness = AnalysisCompleteness.Partial;
            }
            else
            {
                references.AddRange(LoadUnityManagedReferences(model.Project.Options.UnityManagedDir));
            }
        }

        foreach (var precompiledReference in context.Metadata.PrecompiledReferences)
        {
            if (!model.Project.PluginFilesByName.TryGetValue(precompiledReference, out var pluginPath))
            {
                contracts.Add(DiagnosticPolicy.PrecompiledReferenceMissing(context.Name, precompiledReference));
                completeness = AnalysisCompleteness.Partial;
                continue;
            }
            references.Add(MetadataReference.CreateFromFile(pluginPath));
        }

        diagnostics = contracts;
        return references;
    }

    private static bool AssemblyNeedsUnityManagedMetadata(ResolvedProjectModel model, AssemblyContext context)
    {
        var assemblyFiles = model.AssemblyByFile
            .Where(item => item.Value == context.Name)
            .Select(item => item.Key)
            .ToArray();
        if (assemblyFiles.Length == 0)
        {
            return false;
        }

        foreach (var file in assemblyFiles)
        {
            var text = File.ReadAllText(file);
            if (text.Contains("using UnityEngine;", StringComparison.Ordinal)
                || text.Contains("using UnityEditor;", StringComparison.Ordinal)
                || text.Contains(": MonoBehaviour", StringComparison.Ordinal)
                || text.Contains(": ScriptableObject", StringComparison.Ordinal))
            {
                return true;
            }
        }
        return false;
    }

    private static IEnumerable<PortableExecutableReference> LoadUnityManagedReferences(string managedDir)
    {
        if (!Directory.Exists(managedDir))
        {
            return [];
        }
        return Directory.EnumerateFiles(managedDir, "*.dll", SearchOption.TopDirectoryOnly)
            .Select(path => (PortableExecutableReference)MetadataReference.CreateFromFile(path));
    }

    private static PortableExecutableReference[] BasicReferences()
    {
        var trustedAssemblies = ((string?)AppContext.GetData("TRUSTED_PLATFORM_ASSEMBLIES"))
            ?.Split(Path.PathSeparator)
            ?? [];
        return trustedAssemblies
            .Where(path => Path.GetFileName(path) is "System.Private.CoreLib.dll" or "System.Runtime.dll" or "System.Console.dll" or "netstandard.dll")
            .Select(path => (PortableExecutableReference)MetadataReference.CreateFromFile(path))
            .ToArray();
    }
}
