using Xunit;

public class AsmdefGraphResolverTests
{
    [Fact]
    public void Resolve_CreatesDefaultAssemblyContextForFilesWithoutAsmdef()
    {
        const string projectDir = @"C:\repo";
        var sourceFile = @"C:\repo\Assets\Scripts\GameplayType.cs";
        var project = new UnityProjectModel(
            projectDir,
            [sourceFile],
            [],
            [],
            new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase),
            null,
            new Dictionary<string, string>(StringComparer.Ordinal),
            new AnalyzerOptions(projectDir, false, null, false, new HashSet<string>(StringComparer.Ordinal)));

        var resolved = AsmdefGraphResolver.Resolve(project);

        Assert.Equal("Assembly-CSharp", resolved.AssemblyByFile[sourceFile]);
        Assert.True(resolved.AssembliesByName.ContainsKey("Assembly-CSharp"));
        Assert.True(resolved.AssembliesByName["Assembly-CSharp"].IncludeInCompilation);
    }

    [Theory]
    [InlineData(@"C:\repo\build\Generated.cs")]
    [InlineData(@"C:\repo\obj\Debug\net8.0\GeneratedAssemblyInfo.cs")]
    [InlineData(@"C:\repo\bin\Debug\net8.0\GeneratedGlobalUsings.g.cs")]
    public void UnityPaths_HasSkippedPart_RejectsBuildArtifactDirectories(string sourceFile)
    {
        Assert.True(UnityPaths.HasSkippedPart(@"C:\repo", sourceFile));
    }

    [Fact]
    public void Resolve_MapsAsmrefFolderIntoReferencedAssembly()
    {
        var projectDir = @"C:\repo";
        var runtime = new AssemblyDefinition(
            "Project.Runtime",
            "Project.Runtime",
            [],
            AsmdefMetadata.Empty(),
            @"C:\repo\Assets\Runtime",
            "runtime-guid");
        var asmref = new AssemblyReferenceDefinition("GUID:runtime-guid", @"C:\repo\Assets\Features", @"C:\repo\Assets\Features\Feature.asmref");
        var project = new UnityProjectModel(
            projectDir,
            [@"C:\repo\Assets\Features\GameplayFeature.cs"],
            [runtime],
            [asmref],
            new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase),
            null,
            new Dictionary<string, string>(StringComparer.Ordinal),
            new AnalyzerOptions(projectDir, false, null, false, new HashSet<string>(StringComparer.Ordinal)));

        var resolved = AsmdefGraphResolver.Resolve(project);

        Assert.Equal("Project.Runtime", resolved.AssemblyByFile[@"C:\repo\Assets\Features\GameplayFeature.cs"]);
    }

    [Fact]
    public void Resolve_ConvertsGuidReferenceToAssemblyName()
    {
        var projectDir = @"C:\repo";
        var runtime = new AssemblyDefinition(
            "Project.Runtime",
            "Project.Runtime",
            [],
            AsmdefMetadata.Empty(),
            @"C:\repo\Assets\Runtime",
            "runtime-guid");
        var editor = new AssemblyDefinition(
            "Project.Editor",
            "Project.Editor",
            ["GUID:runtime-guid"],
            AsmdefMetadata.Empty(),
            @"C:\repo\Assets\Editor",
            "editor-guid");
        var project = new UnityProjectModel(
            projectDir,
            [@"C:\repo\Assets\Editor\EditorController.cs"],
            [runtime, editor],
            [],
            new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase),
            null,
            new Dictionary<string, string>(StringComparer.Ordinal),
            new AnalyzerOptions(projectDir, false, null, false, new HashSet<string>(StringComparer.Ordinal)));

        var resolved = AsmdefGraphResolver.Resolve(project);

        Assert.Equal(["Project.Runtime"], resolved.AssembliesByName["Project.Editor"].References);
    }

    [Fact]
    public void Resolve_EvaluatesDefineConstraintsAgainstUnityVersion()
    {
        var projectDir = @"C:\repo";
        var asmdef = new AssemblyDefinition(
            "Project.Editor",
            "Project.Editor",
            [],
            new AsmdefMetadata(
                ["Editor"],
                [],
                ["UNITY_2022_3_OR_NEWER", "!DISABLE_EDITOR"],
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
        Assert.DoesNotContain(
            resolved.AssembliesByName["Project.Editor"].Diagnostics,
            diagnostic => diagnostic.Code == "asmdef-define-constraints-not-evaluated");
    }
}
