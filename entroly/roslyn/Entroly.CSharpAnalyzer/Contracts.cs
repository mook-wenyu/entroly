using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.CodeAnalysis;

internal static class AnalysisCompleteness
{
    public const string Complete = "complete";
    public const string Partial = "partial";
    public const string Unsupported = "unsupported";

    public static string Combine(IEnumerable<string> values)
    {
        var result = Complete;
        foreach (var value in values)
        {
            if (value == Unsupported)
            {
                return Unsupported;
            }
            if (value == Partial)
            {
                result = Partial;
            }
        }
        return result;
    }
}

internal sealed record AnalyzerResult(
    string Status,
    string ProjectDir,
    string AnalysisCompleteness,
    IReadOnlyList<ModuleContract> Modules);

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
    string AnalysisCompleteness,
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

internal sealed class AsmrefDocument
{
    [JsonPropertyName("reference")]
    public string Reference { get; init; } = "";
}

internal sealed record AnalyzerOptions(
    string ProjectDir,
    bool Strict,
    string? UnityManagedDir,
    bool HasExplicitDefineSymbols,
    IReadOnlySet<string> ExplicitDefineSymbols)
{
    public static AnalyzerOptions Parse(string[] args)
    {
        var strict = false;
        string? projectDir = null;
        foreach (var arg in args)
        {
            if (string.Equals(arg, "--strict", StringComparison.Ordinal))
            {
                strict = true;
                continue;
            }
            if (projectDir is null)
            {
                projectDir = Path.GetFullPath(arg);
                continue;
            }
            throw new AnalyzerException("用法：Entroly.CSharpAnalyzer [--strict] <project-directory>");
        }

        if (projectDir is null)
        {
            throw new AnalyzerException("用法：Entroly.CSharpAnalyzer [--strict] <project-directory>");
        }
        if (!Directory.Exists(projectDir))
        {
            throw new AnalyzerException($"项目目录不存在：{projectDir}");
        }

        var managedDir = Environment.GetEnvironmentVariable("ENTROLY_UNITY_MANAGED_DIR");
        var rawDefines = Environment.GetEnvironmentVariable("ENTROLY_UNITY_DEFINE_SYMBOLS");
        var hasExplicitDefineSymbols = rawDefines is not null;
        var explicitDefineSymbols = (rawDefines ?? "")
            .Split([',', ';', '\r', '\n'], StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries)
            .ToHashSet(StringComparer.Ordinal);

        return new AnalyzerOptions(
            projectDir,
            strict,
            string.IsNullOrWhiteSpace(managedDir) ? null : Path.GetFullPath(managedDir),
            hasExplicitDefineSymbols,
            explicitDefineSymbols);
    }
}

internal sealed record UnityProjectModel(
    string ProjectDir,
    IReadOnlyList<string> SourceFiles,
    IReadOnlyList<AssemblyDefinition> AssemblyDefinitions,
    IReadOnlyList<AssemblyReferenceDefinition> AssemblyReferences,
    IReadOnlyDictionary<string, string> PluginFilesByName,
    string? ProjectVersion,
    IReadOnlyDictionary<string, string> PackageVersions,
    AnalyzerOptions Options);

internal sealed record AssemblyReferenceDefinition(
    string Reference,
    string Directory,
    string SourcePath);

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
            UnityPaths.ReadUnityMetaGuid(asmdefPath));
    }
}

internal sealed record AssemblyContext(
    string Name,
    string RootNamespace,
    string[] References,
    AsmdefMetadata Metadata,
    string Directory,
    IReadOnlyList<DiagnosticContract> Diagnostics,
    string AnalysisCompleteness,
    IReadOnlySet<string> EffectiveDefineSymbols,
    bool IncludeInCompilation,
    IReadOnlyList<PortableExecutableReference> MetadataReferences)
{
    public static AssemblyContext Default() => new(
        "Assembly-CSharp",
        "",
        [],
        AsmdefMetadata.Empty(),
        "",
        [],
        global::AnalysisCompleteness.Partial,
        new HashSet<string>(StringComparer.Ordinal),
        true,
        []);
}

internal sealed record ResolvedProjectModel(
    UnityProjectModel Project,
    IReadOnlyDictionary<string, AssemblyContext> AssembliesByName,
    IReadOnlyDictionary<string, string> AssemblyByFile);

internal sealed class AnalyzerException(string message) : Exception(message);
