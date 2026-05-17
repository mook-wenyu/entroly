using System.Text.Json;

internal static class UnityProjectScanner
{
    public static UnityProjectModel Scan(AnalyzerOptions options)
    {
        var projectDir = options.ProjectDir;
        var sourceFiles = Directory.EnumerateFiles(projectDir, "*.cs", SearchOption.AllDirectories)
            .Where(path => !UnityPaths.HasSkippedPart(projectDir, path))
            .OrderBy(path => UnityPaths.RelativePath(projectDir, path), StringComparer.OrdinalIgnoreCase)
            .ToArray();
        var asmdefs = Directory.EnumerateFiles(projectDir, "*.asmdef", SearchOption.AllDirectories)
            .Where(path => !UnityPaths.HasSkippedPart(projectDir, path))
            .Select(path => AssemblyDefinition.FromFile(projectDir, path))
            .OrderByDescending(item => item.Directory.Length)
            .ToArray();
        var asmrefs = Directory.EnumerateFiles(projectDir, "*.asmref", SearchOption.AllDirectories)
            .Where(path => !UnityPaths.HasSkippedPart(projectDir, path))
            .Select(ParseAsmref)
            .OrderByDescending(item => item.Directory.Length)
            .ToArray();

        return new UnityProjectModel(
            projectDir,
            sourceFiles,
            asmdefs,
            asmrefs,
            ScanPluginFiles(projectDir),
            ReadProjectVersion(projectDir),
            ReadPackageVersions(projectDir),
            options);
    }

    private static AssemblyReferenceDefinition ParseAsmref(string asmrefPath)
    {
        var json = File.ReadAllText(asmrefPath);
        var asmref = JsonSerializer.Deserialize<AsmrefDocument>(json, JsonOptions.Create())
            ?? throw new AnalyzerException($"asmref 无法解析：{asmrefPath}");
        if (string.IsNullOrWhiteSpace(asmref.Reference))
        {
            throw new AnalyzerException($"asmref 缺少 reference：{asmrefPath}");
        }
        return new AssemblyReferenceDefinition(
            asmref.Reference.Trim(),
            Path.GetDirectoryName(Path.GetFullPath(asmrefPath)) ?? "",
            Path.GetFullPath(asmrefPath));
    }

    private static IReadOnlyDictionary<string, string> ScanPluginFiles(string projectDir)
    {
        return Directory.EnumerateFiles(projectDir, "*.dll", SearchOption.AllDirectories)
            .Where(path => !UnityPaths.HasSkippedPart(projectDir, path))
            .Select(path => new KeyValuePair<string, string>(Path.GetFileName(path) ?? "", path))
            .Where(item => item.Key.Length > 0)
            .GroupBy(item => item.Key, StringComparer.OrdinalIgnoreCase)
            .ToDictionary(group => group.Key, group => group.First().Value, StringComparer.OrdinalIgnoreCase);
    }

    private static string? ReadProjectVersion(string projectDir)
    {
        var versionFile = Path.Combine(projectDir, "ProjectSettings", "ProjectVersion.txt");
        if (!File.Exists(versionFile))
        {
            return null;
        }
        foreach (var line in File.ReadLines(versionFile))
        {
            const string prefix = "m_EditorVersion:";
            if (line.StartsWith(prefix, StringComparison.Ordinal))
            {
                var value = line[prefix.Length..].Trim();
                return string.IsNullOrWhiteSpace(value) ? null : value;
            }
        }
        return null;
    }

    private static IReadOnlyDictionary<string, string> ReadPackageVersions(string projectDir)
    {
        var lockPath = Path.Combine(projectDir, "Packages", "packages-lock.json");
        if (!File.Exists(lockPath))
        {
            return new Dictionary<string, string>(StringComparer.Ordinal);
        }

        using var document = JsonDocument.Parse(File.ReadAllText(lockPath));
        if (!document.RootElement.TryGetProperty("dependencies", out var dependencies))
        {
            return new Dictionary<string, string>(StringComparer.Ordinal);
        }

        var versions = new Dictionary<string, string>(StringComparer.Ordinal);
        foreach (var entry in dependencies.EnumerateObject())
        {
            if (entry.Value.TryGetProperty("version", out var versionElement))
            {
                var version = versionElement.GetString();
                if (!string.IsNullOrWhiteSpace(version))
                {
                    versions[entry.Name] = version.Trim();
                }
            }
        }
        return versions;
    }
}
