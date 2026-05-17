using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;

internal static class CompilationFactory
{
    public static IReadOnlyDictionary<string, SyntaxTree> ParseTrees(UnityProjectModel project)
    {
        var trees = new Dictionary<string, SyntaxTree>(StringComparer.OrdinalIgnoreCase);
        foreach (var file in project.SourceFiles)
        {
            var relativePath = UnityPaths.RelativePath(project.ProjectDir, file);
            var text = File.ReadAllText(file);
            trees[relativePath] = CSharpSyntaxTree.ParseText(text, path: relativePath, encoding: System.Text.Encoding.UTF8);
        }
        return trees;
    }

    public static CSharpCompilation CreateForAssembly(
        UnityProjectModel project,
        ResolvedProjectModel resolved,
        IReadOnlyDictionary<string, SyntaxTree> treesByRelativePath,
        AssemblyContext assembly)
    {
        var assemblyFiles = resolved.AssemblyByFile
            .Where(item => item.Value == assembly.Name)
            .Select(item => treesByRelativePath[UnityPaths.RelativePath(project.ProjectDir, item.Key)])
            .ToArray();
        var contextAssemblyNames = ReferencedAssemblyClosure(assembly, resolved.AssembliesByName);
        var contextFiles = resolved.AssemblyByFile
            .Where(item => contextAssemblyNames.Contains(item.Value))
            .Select(item => treesByRelativePath[UnityPaths.RelativePath(project.ProjectDir, item.Key)])
            .ToArray();

        return CSharpCompilation.Create(
            assembly.Name,
            syntaxTrees: contextFiles.Length > 0 ? contextFiles : assemblyFiles,
            references: assembly.MetadataReferences,
            options: new CSharpCompilationOptions(
                OutputKind.DynamicallyLinkedLibrary,
                allowUnsafe: assembly.Metadata.AllowUnsafeCode));
    }

    private static ISet<string> ReferencedAssemblyClosure(
        AssemblyContext root,
        IReadOnlyDictionary<string, AssemblyContext> assembliesByName)
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
}
