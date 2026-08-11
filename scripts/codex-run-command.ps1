[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RunDirectory,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^\d{3}$')]
    [string]$StepId,

    [Parameter(Mandatory = $true)]
    [string]$Description,

    [Parameter(Mandatory = $true)]
    [string]$Command,

    [Parameter(Mandatory = $true)]
    [string]$WorkingDirectory,

    [int[]]$ExpectedExitCodes = @(0),

    [switch]$Sensitive,

    [ValidateRange(1, 1000000)]
    [int]$InlineLineLimit = 200,

    [ValidateRange(1, 104857600)]
    [int]$InlineByteLimit = 65536
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

function Get-LineCount {
    param([Parameter(Mandatory = $true)][string]$Path)

    if ((Get-Item -LiteralPath $Path).Length -eq 0) {
        return 0
    }

    $count = 0
    foreach ($line in [IO.File]::ReadLines($Path)) {
        $count++
    }
    return $count
}

function Get-IndentedText {
    param([AllowEmptyString()][string]$Text)

    if ([string]::IsNullOrEmpty($Text)) {
        return '    (empty)'
    }

    $lines = $Text -split '\r?\n'
    return (($lines | ForEach-Object { '    ' + $_ }) -join [Environment]::NewLine)
}

function Get-StreamSection {
    param(
        [Parameter(Mandatory = $true)][string]$Label,
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][long]$Bytes,
        [Parameter(Mandatory = $true)][int]$Lines,
        [Parameter(Mandatory = $true)][string]$Sha256,
        [Parameter(Mandatory = $true)][bool]$IsSensitive
    )

    $relativePath = Join-Path 'raw' ([IO.Path]::GetFileName($Path))
    $header = @"
#### $Label

- Pad: $relativePath
- Bytes: $Bytes
- Regels: $Lines
- SHA-256: $Sha256
"@

    if ($IsSensitive) {
        return $header + [Environment]::NewLine + '    [REDACTED SENSITIVE STEP]' + [Environment]::NewLine
    }

    if ($Lines -le $InlineLineLimit -and $Bytes -le $InlineByteLimit) {
        $content = [IO.File]::ReadAllText($Path)
        return $header + [Environment]::NewLine + (Get-IndentedText -Text $content) + [Environment]::NewLine
    }

    $first = @([IO.File]::ReadLines($Path) | Select-Object -First 20)
    $last = @(Get-Content -LiteralPath $Path -Encoding UTF8 -Tail 20)
    $summary = @"

Uitvoer overschrijdt de inlinegrens. Het raw-bestand is volledig bewaard.

Eerste 20 regels:

$(Get-IndentedText -Text (($first | ForEach-Object { [string]$_ }) -join [Environment]::NewLine))

Laatste 20 regels:

$(Get-IndentedText -Text (($last | ForEach-Object { [string]$_ }) -join [Environment]::NewLine))
"@
    return $header + $summary + [Environment]::NewLine
}

$runFull = [IO.Path]::GetFullPath($RunDirectory)
$workFull = [IO.Path]::GetFullPath($WorkingDirectory)
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
if (-not (Test-Path -LiteralPath $workFull -PathType Container)) {
    throw "WorkingDirectory does not exist: $workFull"
}
if ($ExpectedExitCodes.Count -eq 0) {
    throw 'ExpectedExitCodes must contain at least one value.'
}

$commandPath = Join-Path $rawDirectory ($StepId + '-command.txt')
$stdoutPath = Join-Path $rawDirectory ($StepId + '-stdout.txt')
$stderrPath = Join-Path $rawDirectory ($StepId + '-stderr.txt')
$metaPath = Join-Path $rawDirectory ($StepId + '-meta.json')

foreach ($path in @($commandPath, $stdoutPath, $stderrPath, $metaPath)) {
    if (Test-Path -LiteralPath $path) {
        throw "Step evidence already exists and will not be overwritten: $path"
    }
}

$storedCommand = if ($Sensitive) { '[REDACTED SENSITIVE STEP]' } else { $Command }
Write-Utf8NoBom -Path $commandPath -Content $storedCommand

$start = [DateTimeOffset]::Now
$stopwatch = [Diagnostics.Stopwatch]::StartNew()
$stdout = ''
$stderr = ''
$actualExitCode = -998

try {
    $preamble = @'
$utf8 = New-Object System.Text.UTF8Encoding($false)
[Console]::OutputEncoding = $utf8
[Console]::InputEncoding = $utf8
$OutputEncoding = $utf8
$ProgressPreference = 'SilentlyContinue'
$ErrorActionPreference = 'Stop'
$global:LASTEXITCODE = 0
try {
'@
    $postamble = @'
    if ($null -ne $global:LASTEXITCODE) {
        exit [int]$global:LASTEXITCODE
    }
    exit 0
}
catch {
    [Console]::Error.WriteLine($_.Exception.ToString())
    exit 1
}
'@
    $wrappedCommand = $preamble + [Environment]::NewLine + $Command +
        [Environment]::NewLine + $postamble
    $encodedCommand = [Convert]::ToBase64String(
        [Text.Encoding]::Unicode.GetBytes($wrappedCommand)
    )

    $processPath = (Get-Process -Id $PID).Path
    $startInfo = New-Object Diagnostics.ProcessStartInfo
    $startInfo.FileName = $processPath
    $startInfo.Arguments = '-NoLogo -NoProfile -NonInteractive -EncodedCommand ' + $encodedCommand
    $startInfo.WorkingDirectory = $workFull
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $startInfo.StandardOutputEncoding = $utf8NoBom
    $startInfo.StandardErrorEncoding = $utf8NoBom

    $process = New-Object Diagnostics.Process
    $process.StartInfo = $startInfo
    if (-not $process.Start()) {
        throw 'Child PowerShell process did not start.'
    }

    $stdoutTask = $process.StandardOutput.ReadToEndAsync()
    $stderrTask = $process.StandardError.ReadToEndAsync()
    $process.WaitForExit()
    $stdout = $stdoutTask.Result
    $stderr = $stderrTask.Result
    $actualExitCode = $process.ExitCode
    $process.Dispose()
}
catch {
    $stderr = $_.Exception.ToString()
    $actualExitCode = -998
}
finally {
    $stopwatch.Stop()
}

$end = [DateTimeOffset]::Now

if ($Sensitive) {
    Write-Utf8NoBom -Path $stdoutPath -Content '[REDACTED SENSITIVE STEP]'
    Write-Utf8NoBom -Path $stderrPath -Content '[REDACTED SENSITIVE STEP]'
}
else {
    Write-Utf8NoBom -Path $stdoutPath -Content $stdout
    Write-Utf8NoBom -Path $stderrPath -Content $stderr
}

$stdoutItem = Get-Item -LiteralPath $stdoutPath
$stderrItem = Get-Item -LiteralPath $stderrPath
$stdoutLines = Get-LineCount -Path $stdoutPath
$stderrLines = Get-LineCount -Path $stderrPath
$stdoutHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $stdoutPath).Hash
$stderrHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $stderrPath).Hash
$isExpected = $ExpectedExitCodes -contains $actualExitCode

$metadata = [ordered]@{
    StepId = $StepId
    Description = $Description
    Command = $storedCommand
    WorkingDirectory = $workFull
    StartTime = $start.ToString('o')
    EndTime = $end.ToString('o')
    DurationMilliseconds = [math]::Round($stopwatch.Elapsed.TotalMilliseconds, 3)
    ExitCode = $actualExitCode
    ExpectedExitCodes = @($ExpectedExitCodes)
    Expected = $isExpected
    Sensitive = [bool]$Sensitive
    Stdout = [ordered]@{
        Path = Join-Path 'raw' ([IO.Path]::GetFileName($stdoutPath))
        Bytes = $stdoutItem.Length
        Lines = $stdoutLines
        Sha256 = if ($Sensitive) { '[REDACTED]' } else { $stdoutHash }
    }
    Stderr = [ordered]@{
        Path = Join-Path 'raw' ([IO.Path]::GetFileName($stderrPath))
        Bytes = $stderrItem.Length
        Lines = $stderrLines
        Sha256 = if ($Sensitive) { '[REDACTED]' } else { $stderrHash }
    }
}
Write-Utf8NoBom -Path $metaPath -Content ($metadata | ConvertTo-Json -Depth 6)

$expectedText = ($ExpectedExitCodes | ForEach-Object { [string]$_ }) -join ', '
$commandForLog = if ($Sensitive) { '[REDACTED SENSITIVE STEP]' } else { $Command }
$entry = @"

## Step $StepId - $Description

- Start: $($start.ToString('o'))
- Einde: $($end.ToString('o'))
- Duur-ms: $([math]::Round($stopwatch.Elapsed.TotalMilliseconds, 3))
- Werkmap: $workFull
- Commando: $commandForLog
- Exitcode: $actualExitCode
- Verwachte exitcodes: $expectedText
- Verwacht resultaat: $(if ($isExpected) { 'ja' } else { 'nee' })
- Metadata: raw/$StepId-meta.json

$(Get-StreamSection -Label 'stdout' -Path $stdoutPath -Bytes $stdoutItem.Length -Lines $stdoutLines -Sha256 $(if ($Sensitive) { '[REDACTED]' } else { $stdoutHash }) -IsSensitive ([bool]$Sensitive))
$(Get-StreamSection -Label 'stderr' -Path $stderrPath -Bytes $stderrItem.Length -Lines $stderrLines -Sha256 $(if ($Sensitive) { '[REDACTED]' } else { $stderrHash }) -IsSensitive ([bool]$Sensitive))
"@

if (-not $isExpected) {
    $entry += [Environment]::NewLine +
        'CLASSIFICATIE: UNEXPECTED_EXIT. Een herstel- of stopbesluit moet als aparte note worden vastgelegd.' +
        [Environment]::NewLine
}
Append-Utf8NoBom -Path $logPath -Content $entry

$expectedLabel = if ($isExpected) { 'yes' } else { 'no' }
Write-Output ('[{0}] exit={1} expected={2} - {3}' -f $StepId, $actualExitCode, $expectedLabel, $Description)

if (-not $isExpected) {
    exit 1
}
exit 0
