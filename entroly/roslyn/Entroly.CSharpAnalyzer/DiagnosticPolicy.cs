internal static class DiagnosticPolicy
{
    public static DiagnosticContract PlatformConflict(string assemblyName)
        => new("asmdef-platform-conflict", "error", assemblyName, "Unity asmdef cannot contain both includePlatforms and excludePlatforms.");

    public static DiagnosticContract UnresolvedAsmdefGuidReference(string assemblyName, string reference)
        => new("asmdef-unresolved-guid-reference", "warning", assemblyName, $"Unity asmdef reference could not be resolved from .asmdef.meta GUID: {reference}");

    public static DiagnosticContract UnresolvedAsmrefGuidReference(string sourcePath, string reference)
        => new("asmref-unresolved-guid-reference", "warning", sourcePath, $"Unity asmref reference could not be resolved from .asmdef.meta GUID: {reference}");

    public static DiagnosticContract DefineConstraintsNotEvaluated(string assemblyName)
        => new("asmdef-define-constraints-not-evaluated", "warning", assemblyName, "defineConstraints are recorded but not fully evaluated by Entroly.");

    public static DiagnosticContract VersionDefinesNotEvaluated(string assemblyName)
        => new("asmdef-version-defines-not-evaluated", "warning", assemblyName, "versionDefines are recorded but not fully evaluated by Entroly.");

    public static DiagnosticContract PrecompiledReferenceMissing(string assemblyName, string reference)
        => new("asmdef-precompiled-reference-missing", "warning", assemblyName, $"precompiledReferences entry could not be resolved to a DLL: {reference}");

    public static DiagnosticContract UnityManagedReferencesMissing(string assemblyName)
        => new("unity-managed-references-not-loaded", "warning", assemblyName, "UnityEngine/UnityEditor metadata references are required but ENTROLY_UNITY_MANAGED_DIR was not provided.");

    public static DiagnosticContract NoEngineReferencesRecorded(string assemblyName)
        => new("asmdef-no-engine-references-recorded", "info", assemblyName, "noEngineReferences is recorded; Entroly does not add UnityEngine or UnityEditor references.");

    public static DiagnosticContract AutoReferencedRecorded(string assemblyName)
        => new("asmdef-auto-referenced-recorded", "info", assemblyName, "autoReferenced=false is recorded; Entroly uses explicit asmdef references only.");

    public static DiagnosticContract AllowUnsafeCodeApplied(string assemblyName)
        => new("asmdef-allow-unsafe-code-applied", "info", assemblyName, "allowUnsafeCode=true is recorded and applied to the Roslyn compilation options for this assembly.");

    public static DiagnosticContract DefineConstraintsUnsatisfied(string assemblyName)
        => new("asmdef-define-constraints-unsatisfied", "error", assemblyName, "Assembly defineConstraints evaluated to false; Unity would exclude this assembly from compilation.");

    public static DiagnosticContract InvalidVersionDefineExpression(string assemblyName, string expression)
        => new("asmdef-version-define-expression-invalid", "error", assemblyName, $"versionDefines expression is invalid: {expression}");
}
