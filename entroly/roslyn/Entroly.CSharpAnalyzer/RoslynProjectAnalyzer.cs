internal static class RoslynProjectAnalyzer
{
    public static AnalyzerResult Run(AnalyzerOptions options)
    {
        var project = UnityProjectScanner.Scan(options);
        var resolved = ReferenceResolver.AttachMetadataReferences(AsmdefGraphResolver.Resolve(project));
        EnsureStrictCompleteness(options, resolved);

        var treesByRelativePath = CompilationFactory.ParseTrees(project);
        var modules = new List<ModuleContract>();
        foreach (var assembly in resolved.AssembliesByName.Values.OrderBy(item => item.Name, StringComparer.Ordinal))
        {
            if (!assembly.IncludeInCompilation)
            {
                continue;
            }

            var assemblyFiles = resolved.AssemblyByFile
                .Where(item => item.Value == assembly.Name)
                .Select(item => item.Key)
                .ToArray();
            if (assemblyFiles.Length == 0)
            {
                continue;
            }

            var compilation = CompilationFactory.CreateForAssembly(project, resolved, treesByRelativePath, assembly);
            foreach (var file in assemblyFiles)
            {
                var tree = treesByRelativePath[UnityPaths.RelativePath(project.ProjectDir, file)];
                var semanticModel = compilation.GetSemanticModel(tree);
                modules.Add(SymbolProjector.AnalyzeModule(project, tree, semanticModel, assembly));
            }
        }

        return new AnalyzerResult(
            "ok",
            project.ProjectDir,
            AnalysisCompleteness.Combine(modules.Select(item => item.AnalysisCompleteness)),
            modules);
    }

    private static void EnsureStrictCompleteness(AnalyzerOptions options, ResolvedProjectModel resolved)
    {
        if (!options.Strict)
        {
            return;
        }

        var incomplete = resolved.AssembliesByName.Values
            .Where(item => item.AnalysisCompleteness != AnalysisCompleteness.Complete)
            .Select(item => $"{item.Name}:{item.AnalysisCompleteness}")
            .OrderBy(item => item, StringComparer.Ordinal)
            .ToArray();
        if (incomplete.Length > 0)
        {
            throw new AnalyzerException($"strict 模式拒绝不完整分析：{string.Join(", ", incomplete)}");
        }
    }
}
