using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

internal static class SymbolProjector
{
    public static ModuleContract AnalyzeModule(
        UnityProjectModel project,
        SyntaxTree tree,
        SemanticModel semanticModel,
        AssemblyContext assembly)
    {
        var root = tree.GetCompilationUnitRoot();
        var relativePath = UnityPaths.NormalizePath(tree.FilePath);
        var entities = new List<EntityContract>();

        foreach (var member in root.DescendantNodes().OfType<MemberDeclarationSyntax>())
        {
            var symbol = semanticModel.GetDeclaredSymbol(member);
            if (symbol is null)
            {
                continue;
            }

            var kind = EntityKind(symbol);
            if (kind is null)
            {
                continue;
            }

            var location = member.GetLocation().GetLineSpan().StartLinePosition.Line + 1;
            entities.Add(new EntityContract(
                EntityName(symbol),
                kind,
                relativePath,
                location,
                Documentation(symbol),
                Signature(symbol),
                SymbolName(symbol),
                ReturnType(symbol),
                Dependencies(symbol)));
        }

        var usings = root.Usings.Select(u => u.Name?.ToString()).Where(x => !string.IsNullOrWhiteSpace(x)).Cast<string>()
            .Distinct(StringComparer.Ordinal)
            .OrderBy(x => x, StringComparer.Ordinal)
            .ToArray();

        return new ModuleContract(
            relativePath,
            Path.GetFileNameWithoutExtension(relativePath),
            "csharp",
            assembly.Name,
            assembly.RootNamespace,
            assembly.References,
            assembly.Metadata,
            assembly.Diagnostics,
            usings,
            entities,
            assembly.AnalysisCompleteness,
            root.GetText().Lines.Count);
    }

    private static string? EntityKind(ISymbol symbol) => symbol switch
    {
        INamedTypeSymbol { TypeKind: TypeKind.Class } => "class",
        INamedTypeSymbol { TypeKind: TypeKind.Struct } => "struct",
        INamedTypeSymbol { TypeKind: TypeKind.Interface } => "interface",
        INamedTypeSymbol { TypeKind: TypeKind.Enum } => "enum",
        IMethodSymbol { MethodKind: MethodKind.Constructor } => "function",
        IMethodSymbol { MethodKind: MethodKind.Ordinary } => "function",
        IPropertySymbol => "property",
        IFieldSymbol { IsConst: true } => "const",
        _ => null,
    };

    private static string EntityName(ISymbol symbol) => symbol switch
    {
        IMethodSymbol { MethodKind: MethodKind.Constructor } method => method.ContainingType.Name,
        _ => symbol.Name,
    };

    private static string Signature(ISymbol symbol) => symbol switch
    {
        IMethodSymbol method => MethodSignature(method),
        IPropertySymbol property => $"{property.Type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")} {property.Name}",
        IFieldSymbol field => $"const {field.Type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")} {field.Name}",
        INamedTypeSymbol type => $"{type.TypeKind.ToString().ToLowerInvariant()} {type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")}",
        _ => symbol.Name,
    };

    private static string MethodSignature(IMethodSymbol method)
    {
        var parameters = string.Join(", ", method.Parameters.Select(parameter =>
            $"{parameter.Type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "")} {parameter.Name}"));
        var name = method.MethodKind == MethodKind.Constructor ? method.ContainingType.Name : method.Name;
        return $"{name}({parameters})";
    }

    private static string SymbolName(ISymbol symbol)
        => symbol.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "");

    private static string ReturnType(ISymbol symbol) => symbol switch
    {
        IMethodSymbol method => method.ReturnType.ToDisplayString(SymbolDisplayFormat.MinimallyQualifiedFormat),
        IPropertySymbol property => property.Type.ToDisplayString(SymbolDisplayFormat.MinimallyQualifiedFormat),
        IFieldSymbol field => field.Type.ToDisplayString(SymbolDisplayFormat.MinimallyQualifiedFormat),
        _ => "",
    };

    private static string[] Dependencies(ISymbol symbol)
    {
        var dependencies = new SortedSet<string>(StringComparer.Ordinal);
        foreach (var type in ReferencedTypes(symbol))
        {
            var text = type.ToDisplayString(SymbolDisplayFormat.FullyQualifiedFormat).Replace("global::", "");
            if (!string.IsNullOrWhiteSpace(text) && !text.StartsWith("System", StringComparison.Ordinal))
            {
                dependencies.Add(text);
            }
        }
        return dependencies.ToArray();
    }

    private static IEnumerable<ITypeSymbol> ReferencedTypes(ISymbol symbol)
    {
        if (symbol is INamedTypeSymbol named)
        {
            if (named.BaseType is not null) yield return named.BaseType;
            foreach (var iface in named.Interfaces) yield return iface;
        }
        else if (symbol is IMethodSymbol method)
        {
            yield return method.ReturnType;
            foreach (var parameter in method.Parameters) yield return parameter.Type;
        }
        else if (symbol is IPropertySymbol property)
        {
            yield return property.Type;
        }
        else if (symbol is IFieldSymbol field)
        {
            yield return field.Type;
        }
    }

    private static string Documentation(ISymbol symbol)
    {
        var xml = symbol.GetDocumentationCommentXml(expandIncludes: false) ?? "";
        return xml.Replace("<summary>", "", StringComparison.OrdinalIgnoreCase)
            .Replace("</summary>", "", StringComparison.OrdinalIgnoreCase)
            .Trim();
    }
}
