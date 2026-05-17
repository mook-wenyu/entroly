using System.Text.Json;

var options = JsonOptions.Create();

try
{
    var analyzerOptions = AnalyzerOptions.Parse(args);
    var result = RoslynProjectAnalyzer.Run(analyzerOptions);
    Console.Out.Write(JsonSerializer.Serialize(result, options));
}
catch (Exception ex)
{
    var error = new AnalyzerError("error", ex.Message);
    Console.Out.Write(JsonSerializer.Serialize(error, options));
    Environment.ExitCode = 1;
}
