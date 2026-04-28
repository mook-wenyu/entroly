using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

var options = JsonOptions.Create();

try
{
    if (args.Length != 1)
    {
        throw new AnalyzerException("用法：Entroly.CSharpAnalyzer <project-directory>");
    }

    var projectDir = Path.GetFullPath(args[0]);
    if (!Directory.Exists(projectDir))
    {
        throw new AnalyzerException($"项目目录不存在：{projectDir}");
    }

    var result = Analyzer.Run(projectDir);
    Console.Out.Write(JsonSerializer.Serialize(result, options));
}
catch (Exception ex)
{
    var error = new AnalyzerError("error", ex.Message);
    Console.Out.Write(JsonSerializer.Serialize(error, options));
    Environment.ExitCode = 1;
}

internal static class Analyzer
{
    private static readonly string[] SkipParts = ["Library", "Temp", "Logs", "UserSettings", ".git", "obj", "bin"];

    public static AnalyzerResult Run(string projectDir)
    {
        var asmdefs = LoadAsmdefs(projectDir);
        var sourceFiles = Directory.EnumerateFiles(projectDir, "*.cs", SearchOption.AllDirectories)
            .Where(path => !HasSkippedPart(projectDir, path))
            .OrderBy(path => RelativePath(projectDir, path), StringComparer.OrdinalIgnoreCase)
            .ToArray();

        var modules = new List<ModuleContract>();
        var treesByFile = new Dictionary<string, SyntaxTree>(StringComparer.OrdinalIgnoreCase);
        foreach (var file in sourceFiles)
        {
            var rel = RelativePath(projectDir, file);
            var text = File.ReadAllText(file);
            treesByFile[rel] = CSharpSyntaxTree.ParseText(text, path: rel, encoding: System.Text.Encoding.UTF8);
        }

        var assemblyByFile = sourceFiles.ToDictionary(
            file => file,
            file => ResolveAssembly(projectDir, file, asmdefs),
            StringComparer.OrdinalIgnoreCase);
        var assemblies = assemblyByFile.Values
            .DistinctBy(info => info.Name)
            .ToList();
        var assembliesByName = assemblies.ToDictionary(info => info.Name, StringComparer.Ordinal);
        if (assemblies.Count == 0)
        {
            assemblies.Add(AssemblyInfo.Default());
        }

        var allReferences = BasicReferences();
        foreach (var assembly in assemblies)
        {
            var assemblyFiles = sourceFiles
                .Where(file => assemblyByFile[file].Name == assembly.Name)
                .ToArray();
            var contextAssemblyNames = ReferencedAssemblyClosure(assembly, assembliesByName);
            var contextFiles = sourceFiles
                .Where(file => contextAssemblyNames.Contains(assemblyByFile[file].Name))
                .Select(file => treesByFile[RelativePath(projectDir, file)])
                .ToArray();
            if (assemblyFiles.Length == 0)
            {
                continue;
            }

            var compilation = CSharpCompilation.Create(
                assembly.Name,
                syntaxTrees: contextFiles,
                references: allReferences,
                options: new CSharpCompilationOptions(
                    OutputKind.DynamicallyLinkedLibrary,
                    allowUnsafe: assembly.Metadata.AllowUnsafeCode));

            foreach (var tree in assemblyFiles.Select(file => treesByFile[RelativePath(projectDir, file)]))
            {
                var semanticModel = compilation.GetSemanticModel(tree);
                modules.Add(AnalyzeModule(projectDir, tree, semanticModel, assembly));
            }
        }

        return new AnalyzerResult("ok", projectDir, modules);
    }

    private static ModuleContract AnalyzeModule(
        string projectDir,
        SyntaxTree tree,
        SemanticModel semanticModel,
        AssemblyInfo assembly)
    {
        var root = tree.GetCompilationUnitRoot();
        var rel = NormalizePath(tree.FilePath);
        var entities = new List<EntityContract>();

        foreach (var member in root.DescendantNodes().OfType<MemberDeclarationSyntax>())
        {
            var symbol = semanticModel.GetDeclaredSymbol(member);
            if (symbol is null)
            {
                continue;
            }

            var kind = EntityKind(symbol);
            if (kind is null)
            {
                continue;
            }

            var location = member.GetLocation().GetLineSpan().StartLinePosition.Line + 1;
            entities.Add(new EntityContract(
                EntityName(symbol),
                kind,
                rel,
                location,
                Documentation(symbol),
                Signature(symbol),
                SymbolName(symbol),
                ReturnType(symbol),
                Dependencies(symbol)));
        }

        var usings = root.Usings.Select(u => u.Name?.ToString()).Where(x => !string.IsNullOrWhiteSpace(x)).Cast<string>()
            .Distinct(StringComparer.Ordinal)
            .OrderBy(x => x, StringComparer.Ordinal)
            .ToArray();

        return new ModuleContract(
            rel,
            Path.GetFileNameWithoutExtension(rel),
            "csharp",
            assembly.Name,
            assembly.RootNamespace,
            assembly.References,
            assembly.Metadata,
            assembly.Diagnostics,
            usings,
            entities,
            root.GetText().Lines.Count);
    }

    private static IReadOnlyList<AssemblyInfo> LoadAsmdefs(string projectDir)
    {
        var definitions = Directory.EnumerateFiles(projectDir, "*.asmdef", SearchOption.AllDirectories)
            .Where(path => !HasSkippedPart(projectDir, path))
            .Select(path => AssemblyDefinition.FromFile(projectDir, path))
            .OrderByDescending(info => info.Directory.Length)
            .ToArray();
        var guidToAssemblyName = definitions
            .Where(info => !string.IsNullOrWhiteSpace(info.Guid))
            .ToDictionary(info => info.Guid, info => info.Name, StringComparer.OrdinalIgnoreCase);
        return definitions.Select(info => info.ToAssemblyInfo(guidToAssemblyName)).ToArray();
    }

    private static AssemblyInfo ResolveAssembly(string projectDir, string sourceFile, IReadOnlyList<AssemblyInfo> asmdefs)
    {
        var sourceDirectory = Path.GetDirectoryName(Path.GetFullPath(sourceFile)) ?? projectDir;
        return asmdefs.FirstOrDefault(info => IsSameOrChild(sourceDirectory, info.Directory)) ?? AssemblyInfo.Default();
    }

    private static ISet<string> ReferencedAssemblyClosure(
        AssemblyInfo root,
        IReadOnlyDictionary<string, AssemblyInfo> assembliesByName)
    {
        var names = new SortedSet<string>(StringComparer.Ordinal) { root.Name };
        var pending = new Queue<string>(root.References);
        while (pending.Count > 0)
        {
            var name = pending.Dequeue();
            if (!names.Add(name))
            {
                continue;
            }
            if (assembliesByName.TryGetValue(name, out var assembly))
            {
                foreach (var reference in assembly.References)
                {
                    pending.Enqueue(reference);
                }
            }
        }
        return names;
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

    private static string? EntityKind(ISymbol symbol) => symbol switch
    {
        INamedTypeSymbol { TypeKind: TypeKind.Class } => "class",
        INamedTypeSymbol { TypeKind: TypeKind.Struct } => "struct",
        INamedTypeSymbol { TypeKind: TypeKind.Interface } => "interface",
        INamedTypeSymbol { TypeKind: TypeKind.Enum } => "enum",
        IMethodSymbol { MethodKind: MethodKind.Constructor } => "function",
        IMethodSymbol { MethodKind: MethodKind.Ordinary } => "function",
        IPropertySymbol => "property",
        IFieldSymbol { IsConst: true } => "const",
        _ => null,
    };

    private static string EntityName(ISymbol symbol) => symbol switch
    {
        IMethodSymbol { MethodKind: MethodKind.Constructor } method => method.ContainingType.Name,
        _ => symbol.Name,
    };

    private static string Signature(ISymbol symbol) => symbol switch
    {
        IMethodSymbol method => MethodSignature(method),
        IPropertySymbol property => $"{property.Type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")} {property.Name}",
        IFieldSymbol field => $"const {field.Type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")} {field.Name}",
        INamedTypeSymbol type => $"{type.TypeKind.ToString().ToLowerInvariant()} {type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")}",
        _ => symbol.Name,
    };

    private static string MethodSignature(IMethodSymbol method)
    {
        var parameters = string.Join(", ", method.Parameters.Select(p =>
            $"{p.Type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")} {p.Name}"));
        var name = method.MethodKind == MethodKind.Constructor ? method.ContainingType.Name : method.Name;
        return $"{name}({parameters})";
    }

    private static string SymbolName(ISymbol symbol)
    {
        return symbol.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "");
    }

    private static string ReturnType(ISymbol symbol) => symbol switch
    {
        IMethodSymbol method => method.ReturnType.ToDisplayString(SymbolDisplayFormat.MinimallyQualifiedFormat),
        IPropertySymbol property => property.Type.ToDisplayString(SymbolDisplayFormat.MinimallyQualifiedFormat),
        IFieldSymbol field => field.Type.ToDisplayString(SymbolDisplayFormat.MinimallyQualifiedFormat),
        _ => "",
    };

    private static string[] Dependencies(ISymbol symbol)
    {
        var dependencies = new SortedSet<string>(StringComparer.Ordinal);
        foreach (var type in ReferencedTypes(symbol))
        {
            var text = type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "");
            if (!string.IsNullOrWhiteSpace(text) && !text.StartsWith("System", StringComparison.Ordinal))
            {
                dependencies.Add(text);
            }
        }
        return dependencies.ToArray();
    }

    private static IEnumerable<ITypeSymbol> ReferencedTypes(ISymbol symbol)
    {
        if (symbol is INamedTypeSymbol named)
        {
            if (named.BaseType is not null) yield return named.BaseType;
            foreach (var iface in named.Interfaces) yield return iface;
        }
        else if (symbol is IMethodSymbol method)
        {
            yield return method.ReturnType;
            foreach (var parameter in method.Parameters) yield return parameter.Type;
        }
        else if (symbol is IPropertySymbol property)
        {
            yield return property.Type;
        }
        else if (symbol is IFieldSymbol field)
        {
            yield return field.Type;
        }
    }

    private static string Documentation(ISymbol symbol)
    {
        var xml = symbol.GetDocumentationCommentXml(expandIncludes: false) ?? "";
        return xml.Replace("<summary>", "", StringComparison.OrdinalIgnoreCase)
            .Replace("</summary>", "", StringComparison.OrdinalIgnoreCase)
            .Trim();
    }

    private static bool HasSkippedPart(string projectDir, string path)
    {
        var rel = RelativePath(projectDir, path);
        var parts = rel.Split('/');
        return parts.Any(part => SkipParts.Contains(part, StringComparer.OrdinalIgnoreCase));
    }

    private static string RelativePath(string projectDir, string path)
    {
        return NormalizePath(Path.GetRelativePath(projectDir, Path.GetFullPath(path)));
    }

    private static string NormalizePath(string path) => path.Replace('\\', '/');

    private static bool IsSameOrChild(string directory, string parent)
    {
        var dir = Path.GetFullPath(directory).TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
        var root = Path.GetFullPath(parent).TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
        return dir.Equals(root, StringComparison.OrdinalIgnoreCase)
            || dir.StartsWith(root + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase)
            || dir.StartsWith(root + Path.AltDirectorySeparatorChar, StringComparison.OrdinalIgnoreCase);
    }
}

internal sealed record AssemblyInfo(
    string Name,
    string RootNamespace,
    string[] References,
    AsmdefMetadata Metadata,
    DiagnosticContract[] Diagnostics,
    string Directory)
{
    public static AssemblyInfo Default() => new("Assembly-CSharp", "", [], AsmdefMetadata.Empty(), [], "");
}

internal sealed record AssemblyDefinition(
    string Name,
    string RootNamespace,
    string[] RawReferences,
    AsmdefMetadata Metadata,
    string Directory,
    string Guid)
{
    public static AssemblyDefinition FromFile(string projectDir, string asmdefPath)
    {
        var json = File.ReadAllText(asmdefPath);
        var asmdef = JsonSerializer.Deserialize<AsmdefDocument>(json, JsonOptions.Create())
            ?? throw new AnalyzerException($"asmdef 无法解析：{asmdefPath}");
        if (string.IsNullOrWhiteSpace(asmdef.Name))
        {
            throw new AnalyzerException($"asmdef 缺少 name：{asmdefPath}");
        }

        return new AssemblyDefinition(
            asmdef.Name,
            asmdef.RootNamespace ?? "",
            asmdef.References,
            AsmdefMetadata.FromDocument(asmdef),
            Path.GetDirectoryName(Path.GetFullPath(asmdefPath)) ?? projectDir,
            ReadUnityMetaGuid(asmdefPath));
    }

    public AssemblyInfo ToAssemblyInfo(IReadOnlyDictionary<string, string> guidToAssemblyName)
    {
        var references = RawReferences
            .Select(reference => ResolveReference(reference, guidToAssemblyName))
            .Where(reference => !string.IsNullOrWhiteSpace(reference))
            .Distinct(StringComparer.Ordinal)
            .OrderBy(reference => reference, StringComparer.Ordinal)
            .ToArray();

        return new AssemblyInfo(Name, RootNamespace, references, Metadata, BuildDiagnostics(references), Directory);
    }

    private DiagnosticContract[] BuildDiagnostics(IReadOnlyList<string> resolvedReferences)
    {
        var diagnostics = new List<DiagnosticContract>();
        if (Metadata.IncludePlatforms.Count > 0 && Metadata.ExcludePlatforms.Count > 0)
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-platform-conflict",
                "error",
                Name,
                "Unity asmdef cannot contain both includePlatforms and excludePlatforms."));
        }

        foreach (var reference in resolvedReferences.Where(r => r.StartsWith("GUID:", StringComparison.OrdinalIgnoreCase)))
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-unresolved-guid-reference",
                "warning",
                Name,
                $"Unity asmdef reference could not be resolved from .asmdef.meta GUID: {reference}"));
        }

        if (Metadata.DefineConstraints.Count > 0)
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-define-constraints-not-evaluated",
                "warning",
                Name,
                "defineConstraints are recorded but not evaluated by Entroly."));
        }

        if (Metadata.VersionDefines.Count > 0)
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-version-defines-not-evaluated",
                "warning",
                Name,
                "versionDefines are recorded but not evaluated by Entroly."));
        }

        if (Metadata.OverrideReferences || Metadata.PrecompiledReferences.Count > 0)
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-precompiled-references-not-loaded",
                "warning",
                Name,
                "precompiledReferences and overrideReferences are recorded but external DLLs are not loaded by Entroly."));
        }

        if (Metadata.NoEngineReferences)
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-no-engine-references-recorded",
                "info",
                Name,
                "noEngineReferences is recorded; Entroly does not add UnityEngine or UnityEditor references."));
        }

        if (!Metadata.AutoReferenced)
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-auto-referenced-recorded",
                "info",
                Name,
                "autoReferenced=false is recorded; Entroly uses explicit asmdef references only."));
        }

        if (Metadata.AllowUnsafeCode)
        {
            diagnostics.Add(new DiagnosticContract(
                "asmdef-allow-unsafe-code-applied",
                "info",
                Name,
                "allowUnsafeCode=true is recorded and applied to the Roslyn compilation options for this assembly."));
        }

        return diagnostics.ToArray();
    }

    private static string ResolveReference(string reference, IReadOnlyDictionary<string, string> guidToAssemblyName)
    {
        var trimmed = reference.Trim();
        const string guidPrefix = "GUID:";
        if (!trimmed.StartsWith(guidPrefix, StringComparison.OrdinalIgnoreCase))
        {
            return trimmed;
        }

        var guid = trimmed[guidPrefix.Length..].Trim();
        return guidToAssemblyName.TryGetValue(guid, out var assemblyName) ? assemblyName : $"{guidPrefix}{guid}";
    }

    private static string ReadUnityMetaGuid(string asmdefPath)
    {
        var metaPath = asmdefPath + ".meta";
        if (!File.Exists(metaPath))
        {
            return "";
        }

        foreach (var line in File.ReadLines(metaPath))
        {
            var trimmed = line.Trim();
            const string prefix = "guid:";
            if (trimmed.StartsWith(prefix, StringComparison.Ordinal))
            {
                return trimmed[prefix.Length..].Trim();
            }
        }
        return "";
    }
}

internal sealed class AsmdefDocument
{
    [JsonPropertyName("name")]
    public string Name { get; init; } = "";

    [JsonPropertyName("rootNamespace")]
    public string? RootNamespace { get; init; }

    [JsonPropertyName("references")]
    public string[] References { get; init; } = [];

    [JsonPropertyName("includePlatforms")]
    public string[] IncludePlatforms { get; init; } = [];

    [JsonPropertyName("excludePlatforms")]
    public string[] ExcludePlatforms { get; init; } = [];

    [JsonPropertyName("defineConstraints")]
    public string[] DefineConstraints { get; init; } = [];

    [JsonPropertyName("versionDefines")]
    public VersionDefineDocument[] VersionDefines { get; init; } = [];

    [JsonPropertyName("precompiledReferences")]
    public string[] PrecompiledReferences { get; init; } = [];

    [JsonPropertyName("overrideReferences")]
    public bool OverrideReferences { get; init; }

    [JsonPropertyName("noEngineReferences")]
    public bool NoEngineReferences { get; init; }

    [JsonPropertyName("autoReferenced")]
    public bool AutoReferenced { get; init; } = true;

    [JsonPropertyName("allowUnsafeCode")]
    public bool AllowUnsafeCode { get; init; }
}

internal sealed class VersionDefineDocument
{
    [JsonPropertyName("name")]
    public string Name { get; init; } = "";

    [JsonPropertyName("expression")]
    public string Expression { get; init; } = "";

    [JsonPropertyName("define")]
    public string Define { get; init; } = "";
}

internal sealed record VersionDefineContract(string Name, string Expression, string Define);

internal sealed record AsmdefMetadata(
    IReadOnlyList<string> IncludePlatforms,
    IReadOnlyList<string> ExcludePlatforms,
    IReadOnlyList<string> DefineConstraints,
    IReadOnlyList<VersionDefineContract> VersionDefines,
    IReadOnlyList<string> PrecompiledReferences,
    bool OverrideReferences,
    bool NoEngineReferences,
    bool AutoReferenced,
    bool AllowUnsafeCode)
{
    public static AsmdefMetadata Empty() => new([], [], [], [], [], false, false, true, false);

    public static AsmdefMetadata FromDocument(AsmdefDocument document)
    {
        return new AsmdefMetadata(
            Clean(document.IncludePlatforms),
            Clean(document.ExcludePlatforms),
            Clean(document.DefineConstraints),
            document.VersionDefines
                .Select(item => new VersionDefineContract(item.Name.Trim(), item.Expression.Trim(), item.Define.Trim()))
                .Where(item => !string.IsNullOrWhiteSpace(item.Name) || !string.IsNullOrWhiteSpace(item.Expression) || !string.IsNullOrWhiteSpace(item.Define))
                .ToArray(),
            Clean(document.PrecompiledReferences),
            document.OverrideReferences,
            document.NoEngineReferences,
            document.AutoReferenced,
            document.AllowUnsafeCode);
    }

    private static string[] Clean(IEnumerable<string> values)
    {
        return values
            .Select(value => value.Trim())
            .Where(value => !string.IsNullOrWhiteSpace(value))
            .Distinct(StringComparer.Ordinal)
            .OrderBy(value => value, StringComparer.Ordinal)
            .ToArray();
    }
}

internal sealed record AnalyzerResult(string Status, string ProjectDir, IReadOnlyList<ModuleContract> Modules);
internal sealed record AnalyzerError(string Status, string Error);
internal sealed record ModuleContract(
    string Path,
    string Name,
    string Language,
    string Assembly,
    string RootNamespace,
    IReadOnlyList<string> AssemblyReferences,
    AsmdefMetadata Asmdef,
    IReadOnlyList<DiagnosticContract> Diagnostics,
    IReadOnlyList<string> Imports,
    IReadOnlyList<EntityContract> Entities,
    int Loc);
internal sealed record DiagnosticContract(string Code, string Severity, string Assembly, string Message);
internal sealed record EntityContract(
    string Name,
    string Kind,
    string FilePath,
    int Line,
    string Docstring,
    string Signature,
    string Symbol,
    string ReturnType,
    IReadOnlyList<string> Dependencies);
internal sealed class AnalyzerException(string message) : Exception(message);

internal static class JsonOptions
{
    public static JsonSerializerOptions Create()
    {
        return new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
            DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
        };
    }
}
