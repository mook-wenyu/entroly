using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Xunit;

public class CompilationFactoryTests
{
    [Fact]
    public void CreateForAssembly_IncludesTransitiveAssemblyClosure()
    {
        const string projectDir = @"C:\repo";
        var sourceFiles = new[]
        {
            @"C:\repo\Assets\A\AType.cs",
            @"C:\repo\Assets\B\BType.cs",
            @"C:\repo\Assets\C\CType.cs",
        };
        var project = new UnityProjectModel(
            projectDir,
            sourceFiles,
            [],
            [],
            new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase),
            null,
            new Dictionary<string, string>(StringComparer.Ordinal),
            new AnalyzerOptions(projectDir, false, null, false, new HashSet<string>(StringComparer.Ordinal)));

        var parseTrees = new Dictionary<string, SyntaxTree>(StringComparer.OrdinalIgnoreCase)
        {
            ["Assets/A/AType.cs"] = Microsoft.CodeAnalysis.CSharp.CSharpSyntaxTree.ParseText(
                "namespace Project.A; public sealed class AType { }",
                path: "Assets/A/AType.cs"),
            ["Assets/B/BType.cs"] = Microsoft.CodeAnalysis.CSharp.CSharpSyntaxTree.ParseText(
                "using Project.A; namespace Project.B; public sealed class BType { public AType Create() => new(); }",
                path: "Assets/B/BType.cs"),
            ["Assets/C/CType.cs"] = Microsoft.CodeAnalysis.CSharp.CSharpSyntaxTree.ParseText(
                "using Project.B; namespace Project.C; public sealed class CType { public BType Create() => new(); }",
                path: "Assets/C/CType.cs"),
        };

        var assemblies = new Dictionary<string, AssemblyContext>(StringComparer.Ordinal)
        {
            ["Project.A"] = new(
                "Project.A",
                "Project.A",
                [],
                AsmdefMetadata.Empty(),
                @"C:\repo\Assets\A",
                [],
                AnalysisCompleteness.Complete,
                new HashSet<string>(StringComparer.Ordinal),
                true,
                BasicReferences()),
            ["Project.B"] = new(
                "Project.B",
                "Project.B",
                ["Project.A"],
                AsmdefMetadata.Empty(),
                @"C:\repo\Assets\B",
                [],
                AnalysisCompleteness.Complete,
                new HashSet<string>(StringComparer.Ordinal),
                true,
                BasicReferences()),
            ["Project.C"] = new(
                "Project.C",
                "Project.C",
                ["Project.B"],
                AsmdefMetadata.Empty(),
                @"C:\repo\Assets\C",
                [],
                AnalysisCompleteness.Complete,
                new HashSet<string>(StringComparer.Ordinal),
                true,
                BasicReferences()),
        };

        var resolved = new ResolvedProjectModel(
            project,
            assemblies,
            new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase)
            {
                [@"C:\repo\Assets\A\AType.cs"] = "Project.A",
                [@"C:\repo\Assets\B\BType.cs"] = "Project.B",
                [@"C:\repo\Assets\C\CType.cs"] = "Project.C",
            });

        var compilation = CompilationFactory.CreateForAssembly(project, resolved, parseTrees, assemblies["Project.C"]);
        var tree = parseTrees["Assets/C/CType.cs"];
        var semanticModel = compilation.GetSemanticModel(tree);
        var returnType = tree.GetRoot()
            .DescendantNodes()
            .OfType<MethodDeclarationSyntax>()
            .Single()
            .ReturnType;
        var symbol = semanticModel.GetTypeInfo(returnType).Type;

        Assert.NotNull(symbol);
        Assert.Equal("Project.B.BType", symbol!.ToDisplayString());
    }

    [Fact]
    public void Resolve_EvaluatesOrDefineConstraintWhenAnyBranchMatches()
    {
        var projectDir = @"C:\repo";
        var asmdef = new AssemblyDefinition(
            "Project.Editor",
            "Project.Editor",
            [],
            new AsmdefMetadata(
                ["Editor"],
                [],
                ["DISABLE_EDITOR || UNITY_2022_3_OR_NEWER"],
                [],
                [],
                false,
                true,
                true,
                false),
            @"C:\repo\Assets\Editor",
            "editor-guid");
        var project = new UnityProjectModel(
            projectDir,
            [@"C:\repo\Assets\Editor\EditorController.cs"],
            [asmdef],
            [],
            new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase),
            "2022.3.20f1",
            new Dictionary<string, string>(StringComparer.Ordinal),
            new AnalyzerOptions(projectDir, false, null, true, new HashSet<string>(StringComparer.Ordinal)));

        var resolved = AsmdefGraphResolver.Resolve(project);

        Assert.True(resolved.AssembliesByName["Project.Editor"].IncludeInCompilation);
    }

    private static IReadOnlyList<PortableExecutableReference> BasicReferences()
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
