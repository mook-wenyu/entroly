using Xunit;

public class DiagnosticPolicyTests
{
    [Fact]
    public void PrecompiledReferenceMissing_UsesSpecificDiagnosticCode()
    {
        var diagnostic = DiagnosticPolicy.PrecompiledReferenceMissing("Project.Editor", "Plugin.dll");

        Assert.Equal("asmdef-precompiled-reference-missing", diagnostic.Code);
        Assert.Equal("warning", diagnostic.Severity);
        Assert.Contains("Plugin.dll", diagnostic.Message);
    }

    [Fact]
    public void InvalidVersionDefineExpression_UsesErrorSeverity()
    {
        var diagnostic = DiagnosticPolicy.InvalidVersionDefineExpression("Project.Editor", "[oops");

        Assert.Equal("asmdef-version-define-expression-invalid", diagnostic.Code);
        Assert.Equal("error", diagnostic.Severity);
    }
}
