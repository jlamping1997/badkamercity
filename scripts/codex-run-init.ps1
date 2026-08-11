[CmdletBinding(DefaultParameterSetName = 'RequestText')]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[A-Za-z0-9][A-Za-z0-9._-]*$')]
    [string]$TaskId,

    [Parameter(Mandatory = $true)]
    [string]$BaseDirectory,

    [Parameter(Mandatory = $true, ParameterSetName = 'RequestFile')]
    [string]$RequestFile,

    [Parameter(Mandatory = $true, ParameterSetName = 'RequestText')]
    [AllowEmptyString()]
    [string]$RequestText,

    [Parameter(Mandatory = $true)]
    [string[]]$AllowedPaths,

    [ValidatePattern('^[A-Za-z0-9][A-Za-z0-9._-]*$')]
    [string]$RunId
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Content
    )

    [IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Get-GitValue {
    param([string[]]$Arguments)

    $output = @(& git -C $baseFull @Arguments 2>$null)
    if ($LASTEXITCODE -ne 0) {
        return '[NOT AVAILABLE]'
    }
    return (($output | ForEach-Object { [string]$_ }) -join [Environment]::NewLine).Trim()
}

$baseFull = [IO.Path]::GetFullPath($BaseDirectory)
if (-not (Test-Path -LiteralPath $baseFull -PathType Container)) {
    throw "BaseDirectory does not exist: $baseFull"
}

if ([string]::IsNullOrWhiteSpace($RunId)) {
    $RunId = '{0}_{1}' -f $TaskId, (Get-Date -Format 'yyyyMMdd-HHmmss')
}

$runsRoot = Join-Path $baseFull 'docs\_codex_runs'
$runDirectory = Join-Path $runsRoot $RunId
$rawDirectory = Join-Path $runDirectory 'raw'
[IO.Directory]::CreateDirectory($rawDirectory) | Out-Null

$requestPath = Join-Path $runDirectory '00_REQUEST.txt'
$contextPath = Join-Path $runDirectory '01_CONTEXT.md'
$logPath = Join-Path $runDirectory 'FULL_EXECUTION_LOG.md'
$changesPath = Join-Path $runDirectory 'CHANGES.md'
$finalReportPath = Join-Path $runDirectory 'FINAL_REPORT.md'
$manifestPath = Join-Path $runDirectory 'UPLOAD_MANIFEST.md'

if ($PSCmdlet.ParameterSetName -eq 'RequestFile') {
    $requestFull = [IO.Path]::GetFullPath($RequestFile)
    if (-not (Test-Path -LiteralPath $requestFull -PathType Leaf)) {
        throw "RequestFile does not exist: $requestFull"
    }
    $requestContent = [IO.File]::ReadAllText($requestFull)
}
else {
    $requestContent = $RequestText
}

if (-not (Test-Path -LiteralPath $requestPath -PathType Leaf) -or
    (Get-Item -LiteralPath $requestPath).Length -eq 0) {
    Write-Utf8NoBom -Path $requestPath -Content $requestContent
}

$branch = Get-GitValue -Arguments @('branch', '--show-current')
$head = Get-GitValue -Arguments @('rev-parse', 'HEAD')
$originMain = Get-GitValue -Arguments @('rev-parse', 'origin/main')
$gitStatus = Get-GitValue -Arguments @('status', '--porcelain=v1', '--untracked-files=all')
$gitVersion = ((& git --version 2>$null) -join '').Trim()
$localTime = (Get-Date).ToString('o')
$utcTime = (Get-Date).ToUniversalTime().ToString('o')

if (-not (Test-Path -LiteralPath $contextPath -PathType Leaf)) {
    $allowedLines = ($AllowedPaths | ForEach-Object { '- ' + $_ }) -join [Environment]::NewLine
    $statusText = if ([string]::IsNullOrEmpty($gitStatus)) { 'schoon' } else { $gitStatus }
    $context = @"
# Codex Run Context

| Veld | Waarde |
| --- | --- |
| Run-ID | $RunId |
| Taak-ID | $TaskId |
| Lokale tijd | $localTime |
| UTC-tijd | $utcTime |
| Werkmap | $baseFull |
| Branch | $branch |
| HEAD | $head |
| origin/main | $originMain |
| PowerShell | $($PSVersionTable.PSVersion.ToString()) |
| Git | $gitVersion |

## Initiele Git-status

    $statusText

## Toegestane paden

$allowedLines

Lokale gebruiker en host worden niet automatisch opgeslagen. Credentials,
klant-, order- en persoonsgegevens horen niet in deze runmap.
"@
    Write-Utf8NoBom -Path $contextPath -Content $context
}

if (-not (Test-Path -LiteralPath $logPath -PathType Leaf)) {
    Write-Utf8NoBom -Path $logPath -Content ('# Full Execution Log - ' + $RunId + [Environment]::NewLine)
}
if (-not (Test-Path -LiteralPath $changesPath -PathType Leaf)) {
    Write-Utf8NoBom -Path $changesPath -Content ('# Changes - ' + $RunId + [Environment]::NewLine)
}
if (-not (Test-Path -LiteralPath $finalReportPath -PathType Leaf)) {
    Write-Utf8NoBom -Path $finalReportPath -Content ('# Final Report - ' + $RunId + [Environment]::NewLine)
}
if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    Write-Utf8NoBom -Path $manifestPath -Content ('# Upload Manifest - ' + $RunId + [Environment]::NewLine)
}

$result = [ordered]@{
    RunId = $RunId
    RunDirectory = $runDirectory
    LogPath = $logPath
    RawDirectory = $rawDirectory
}

Write-Output ($result | ConvertTo-Json -Compress)
