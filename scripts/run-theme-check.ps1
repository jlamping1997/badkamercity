[CmdletBinding()]
param()

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

# Shopify CLI 4.6.1 is the approved project baseline, not a claim about the latest available version.
$requiredShopifyCliVersion = '4.6.1'
$repositoryRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$configPath = Join-Path $repositoryRoot '.theme-check.yml'

if (-not (Test-Path -LiteralPath $configPath -PathType Leaf)) {
    [Console]::Error.WriteLine("Theme Check configuration not found: $configPath")
    exit 2
}

$versionOutput = @(& shopify version 2>&1)
$versionExitCode = $LASTEXITCODE
$versionText = (($versionOutput | ForEach-Object { [string]$_ }) -join [Environment]::NewLine).Trim()

foreach ($line in $versionOutput) {
    [Console]::Error.WriteLine([string]$line)
}

if ($versionExitCode -ne 0) {
    [Console]::Error.WriteLine("Unable to verify Shopify CLI version (exit code $versionExitCode).")
    exit $versionExitCode
}

$semanticVersions = @(
    [regex]::Matches($versionText, '(?<![0-9])([0-9]+\.[0-9]+\.[0-9]+)(?![0-9])') |
        ForEach-Object { $_.Groups[1].Value } |
        Sort-Object -Unique
)

if ($semanticVersions.Count -ne 1) {
    [Console]::Error.WriteLine('Unable to determine exactly one semantic Shopify CLI version.')
    exit 2
}

if ($semanticVersions[0] -ne $requiredShopifyCliVersion) {
    [Console]::Error.WriteLine(
        "Shopify CLI version mismatch: found $($semanticVersions[0]); required project baseline is $requiredShopifyCliVersion. No install or update was attempted."
    )
    exit 2
}

& shopify theme check --path $repositoryRoot --no-color --output json
$themeCheckExitCode = $LASTEXITCODE
exit $themeCheckExitCode
