internal static class VersionExpressions
{
    public static bool TryEvaluate(string expression, string version, out bool matches)
    {
        matches = false;
        if (!SemanticVersion.TryParse(version, out var actual))
        {
            return false;
        }
        expression = expression.Trim();
        if (expression.Length == 0)
        {
            return false;
        }

        if ((expression.StartsWith("[", StringComparison.Ordinal) || expression.StartsWith("(", StringComparison.Ordinal))
            && (expression.EndsWith("]", StringComparison.Ordinal) || expression.EndsWith(")", StringComparison.Ordinal)))
        {
            var body = expression[1..^1];
            var commaIndex = body.IndexOf(',');
            if (commaIndex < 0)
            {
                if (!SemanticVersion.TryParse(body.Trim(), out var exact))
                {
                    return false;
                }
                matches = actual.CompareTo(exact) == 0;
                return true;
            }

            var lowerText = body[..commaIndex].Trim();
            var upperText = body[(commaIndex + 1)..].Trim();
            if (!SemanticVersion.TryParse(lowerText, out var lower) || !SemanticVersion.TryParse(upperText, out var upper))
            {
                return false;
            }

            var includeLower = expression[0] == '[';
            var includeUpper = expression[^1] == ']';
            var lowerComparison = actual.CompareTo(lower);
            var upperComparison = actual.CompareTo(upper);
            matches = (includeLower ? lowerComparison >= 0 : lowerComparison > 0)
                && (includeUpper ? upperComparison <= 0 : upperComparison < 0);
            return true;
        }

        if (!SemanticVersion.TryParse(expression, out var minimum))
        {
            return false;
        }

        matches = actual.CompareTo(minimum) >= 0;
        return true;
    }
}

internal sealed record SemanticVersion(int Major, int Minor, int Patch, string Label, int LabelNumber) : IComparable<SemanticVersion>
{
    public static bool TryParse(string text, out SemanticVersion version)
    {
        version = new SemanticVersion(0, 0, 0, "", 0);
        var parts = text.Trim().Split('-', 2, StringSplitOptions.TrimEntries);
        var numericParts = parts[0].Split('.', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
        if (numericParts.Length < 2 || numericParts.Length > 3)
        {
            return false;
        }
        if (!int.TryParse(numericParts[0], out var major) || !int.TryParse(numericParts[1], out var minor))
        {
            return false;
        }
        var patch = 0;
        if (numericParts.Length == 3 && !int.TryParse(numericParts[2], out patch))
        {
            return false;
        }

        var label = "";
        var labelNumber = 0;
        if (parts.Length == 2)
        {
            var labelParts = parts[1].Split('.', 2, StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
            label = labelParts[0];
            if (labelParts.Length == 2 && !int.TryParse(labelParts[1], out labelNumber))
            {
                return false;
            }
        }

        version = new SemanticVersion(major, minor, patch, label, labelNumber);
        return true;
    }

    public int CompareTo(SemanticVersion? other)
    {
        if (other is null)
        {
            return 1;
        }
        var comparison = Major.CompareTo(other.Major);
        if (comparison != 0) return comparison;
        comparison = Minor.CompareTo(other.Minor);
        if (comparison != 0) return comparison;
        comparison = Patch.CompareTo(other.Patch);
        if (comparison != 0) return comparison;
        var hasLabel = !string.IsNullOrEmpty(Label);
        var otherHasLabel = !string.IsNullOrEmpty(other.Label);
        if (hasLabel != otherHasLabel)
        {
            return hasLabel ? -1 : 1;
        }
        comparison = string.Compare(Label, other.Label, StringComparison.Ordinal);
        if (comparison != 0) return comparison;
        return LabelNumber.CompareTo(other.LabelNumber);
    }
}
