[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RunDirectory,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^\d{3}$')]
    [string]$StepId,

    [Parameter(Mandatory = $true)]
    [ValidateSet(
        'DECISION',
        'FILE_CHANGE',
        'ERROR',
        'RECOVERY',
        'CONTEXT_RESTORED',
        'HUMAN_INPUT',
        'VALIDATION',
        'SECURITY_REDACTION',
        'PROGRESS'
    )]
    [string]$Category,

    [Parameter(Mandatory = $true)]
    [string]$Title,

    [Parameter(Mandatory = $true)]
    [AllowEmptyString()]
    [string]$Body,

    [string[]]$RelatedFiles = @()
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

function Append-Utf8NoBom {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Content
    )

    [IO.File]::AppendAllText($Path, $Content, $utf8NoBom)
}

$runFull = [IO.Path]::GetFullPath($RunDirectory)
$rawDirectory = Join-Path $runFull 'raw'
$logPath = Join-Path $runFull 'FULL_EXECUTION_LOG.md'

if (-not (Test-Path -LiteralPath $runFull -PathType Container)) {
    throw "RunDirectory does not exist: $runFull"
}
if (-not (Test-Path -LiteralPath $rawDirectory -PathType Container)) {
    throw "Raw directory does not exist: $rawDirectory"
}
if (-not (Test-Path -LiteralPath $logPath -PathType Leaf)) {
    throw "FULL_EXECUTION_LOG.md does not exist: $logPath"
}

$notePath = Join-Path $rawDirectory ($StepId + '-note.md')
if (Test-Path -LiteralPath $notePath) {
    throw "Step evidence already exists and will not be overwritten: $notePath"
}

$timestamp = [DateTimeOffset]::Now.ToString('o')
$relatedText = if ($RelatedFiles.Count -eq 0) {
    '- geen'
}
else {
    ($RelatedFiles | ForEach-Object { '- ' + $_ }) -join [Environment]::NewLine
}

$note = @"
# Note $StepId - $Category - $Title

- Tijd: $timestamp
- Categorie: $Category
- Titel: $Title

## Gerelateerde bestanden

$relatedText

## Inhoud

$Body
"@

Write-Utf8NoBom -Path $notePath -Content $note

$logEntry = @"

## Note $StepId - $Category - $Title

- Tijd: $timestamp
- Raw: raw/$StepId-note.md
- Gerelateerde bestanden:
$relatedText

$Body
"@

Append-Utf8NoBom -Path $logPath -Content $logEntry
Write-Output ('[{0}] note={1} - {2}' -f $StepId, $Category, $Title)
