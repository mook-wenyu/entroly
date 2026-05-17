using Xunit;

public class VersionExpressionsTests
{
    [Theory]
    [InlineData("1.7.0", "1.7.0", true)]
    [InlineData("1.7.0", "1.6.9", false)]
    [InlineData("[1.7,2.0)", "1.7.0", true)]
    [InlineData("[1.7,2.0)", "2.0.0", false)]
    [InlineData("[2.4.5]", "2.4.5", true)]
    [InlineData("[2.4.5]", "2.4.6", false)]
    [InlineData("(0.2.4,5.6.2-preview.2]", "5.6.2-preview.2", true)]
    public void TryEvaluate_ReturnsExpectedResult(string expression, string version, bool expected)
    {
        var parsed = VersionExpressions.TryEvaluate(expression, version, out var matches);

        Assert.True(parsed);
        Assert.Equal(expected, matches);
    }

    [Fact]
    public void TryEvaluate_InvalidExpression_ReturnsFalse()
    {
        var parsed = VersionExpressions.TryEvaluate("bogus", "1.7.0", out var matches);

        Assert.False(parsed);
        Assert.False(matches);
    }
}
