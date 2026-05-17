internal static class UnityPaths
{
    public static readonly string[] SkipParts = [
        "Library",
        "Temp",
        "Logs",
        "UserSettings",
        ".git",
        "target",
        "dist",
        "build",
        "obj",
        "bin",
    ];

    public static bool HasSkippedPart(string projectDir, string path)
    {
        var rel = RelativePath(projectDir, path);
        var parts = rel.Split('/');
        return parts.Any(part => SkipParts.Contains(part, StringComparer.OrdinalIgnoreCase));
    }

    public static string RelativePath(string projectDir, string path)
    {
        return NormalizePath(Path.GetRelativePath(projectDir, Path.GetFullPath(path)));
    }

    public static string NormalizePath(string path) => path.Replace('\\', '/');

    public static bool IsSameOrChild(string directory, string parent)
    {
        var dir = Path.GetFullPath(directory).TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
        var root = Path.GetFullPath(parent).TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
        return dir.Equals(root, StringComparison.OrdinalIgnoreCase)
            || dir.StartsWith(root + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase)
            || dir.StartsWith(root + Path.AltDirectorySeparatorChar, StringComparison.OrdinalIgnoreCase);
    }

    public static string ReadUnityMetaGuid(string assetPath)
    {
        var metaPath = assetPath + ".meta";
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
