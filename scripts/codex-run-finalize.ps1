[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RunDirectory,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[A-Za-z0-9][A-Za-z0-9._-]*$')]
    [string]$TaskId,

    [Parameter(Mandatory = $true)]
    [ValidateSet('DONE', 'REVIEW', 'BLOCKED')]
    [string]$Status,

    [Parameter(Mandatory = $true)]
    [string]$MasterplanVersion,

    [Parameter(Mandatory = $true)]
    [string[]]$UploadPaths,

    [string[]]$PhaseCommitHashes = @(),

    [Parameter(Mandatory = $true)]
    [string]$FinalSummaryFile
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

function Get-RelativePath {
    param(
        [Parameter(Mandatory = $true)][string]$BasePath,
        [Parameter(Mandatory = $true)][string]$TargetPath
    )

    $baseWithSlash = $BasePath.TrimEnd('\', '/') + [IO.Path]::DirectorySeparatorChar
    $baseUri = New-Object Uri($baseWithSlash)
    $targetUri = New-Object Uri($TargetPath)
    return [Uri]::UnescapeDataString(
        $baseUri.MakeRelativeUri($targetUri).ToString()
    ).Replace('\', '/')
}

function Get-UploadState {
    param(
        [Parameter(Mandatory = $true)][string]$RepositoryRoot,
        [Parameter(Mandatory = $true)][string]$RelativePath
    )

    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    & git -C $RepositoryRoot ls-files --error-unmatch -- $RelativePath *> $null
    $trackedExit = $LASTEXITCODE
    if ($trackedExit -eq 0) {
        $ErrorActionPreference = $previousErrorActionPreference
        return 'tracked'
    }

    & git -C $RepositoryRoot check-ignore -q -- $RelativePath *> $null
    $ignoredExit = $LASTEXITCODE
    $ErrorActionPreference = $previousErrorActionPreference
    if ($ignoredExit -eq 0) {
        return 'ignored'
    }
    return 'untracked'
}

function Get-UploadReason {
    param([string]$RelativePath)

    if ($RelativePath -match 'TECHNICAL_STABILIZATION_PLAN|PRODUCT_DATA_CONTRACT') {
        return 'Goedgekeurde fase-A-documentatie.'
    }
    if ($RelativePath -match 'FULL_EXECUTION_LOG') {
        return 'Volledig observeerbaar uitvoeringsbewijs.'
    }
    if ($RelativePath -match 'FINAL_REPORT') {
        return 'Overzicht van fase A, fase B, tests en eindcontroles.'
    }
    if ($RelativePath -match 'UPLOAD_MANIFEST') {
        return 'Controleerbare uploadselectie met paden, groottes en hashes.'
    }
    if ($RelativePath -match 'REVIEW_FILES_MANIFEST') {
        return 'Hashbewijs voor de repositorysnapshots onder review_files/.'
    }
    if ($RelativePath -match '_BUNDLE[.]zip$') {
        return 'Complete lokale runbundle met alle bewijsbestanden en raw-uitvoer.'
    }
    return 'Tracked fase-B-uitvoer voor menselijke review.'
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

function Test-IsPathWithin {
    param(
        [Parameter(Mandatory = $true)][string]$ParentPath,
        [Parameter(Mandatory = $true)][string]$CandidatePath
    )

    $parentFull = [IO.Path]::GetFullPath($ParentPath).TrimEnd('\', '/') +
        [IO.Path]::DirectorySeparatorChar
    $candidateFull = [IO.Path]::GetFullPath($CandidatePath)
    return $candidateFull.StartsWith(
        $parentFull,
        [StringComparison]::OrdinalIgnoreCase
    )
}

function Test-IsForbiddenReviewFile {
    param([Parameter(Mandatory = $true)][string]$RelativePath)

    $normalized = $RelativePath.Replace('\', '/').TrimStart('/')
    $segments = @($normalized -split '/')
    if ($segments -contains '.git') {
        return $true
    }

    $name = [IO.Path]::GetFileName($normalized).ToLowerInvariant()
    if ($name -eq '.env' -or $name.StartsWith('.env.')) {
        return $true
    }
    if ($name -eq 'id_rsa' -or $name.StartsWith('id_rsa.')) {
        return $true
    }
    if ($name.EndsWith('.pem') -or $name.EndsWith('.pfx') -or
        $name.EndsWith('.p12') -or $name.EndsWith('.key')) {
        return $true
    }
    if ($name -match '(^|[._-])private[._-]?key([._-]|$)') {
        return $true
    }
    return $false
}

function Assert-ObjectProperty {
    param(
        [Parameter(Mandatory = $true)]$Object,
        [Parameter(Mandatory = $true)][string]$Name,
        [Parameter(Mandatory = $true)][string]$Context
    )

    if (-not ($Object.PSObject.Properties.Name -contains $Name)) {
        throw "Raw evidence metadata mist $Name in $Context."
    }
}

function Assert-RawEvidence {
    param([Parameter(Mandatory = $true)][string]$RawDirectory)

    $allRawFiles = @(Get-ChildItem -LiteralPath $RawDirectory -File)
    $metaFiles = @($allRawFiles | Where-Object { $_.Name -like '*-meta.json' })
    $noteFiles = @($allRawFiles | Where-Object { $_.Name -like '*-note.md' })
    $metaIds = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)
    $noteIds = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::Ordinal)
    $expectedFailureCount = 0
    $unexpectedFailureCount = 0

    foreach ($metaFile in $metaFiles) {
        if ($metaFile.Name -notmatch '^(\d{3})-meta[.]json$') {
            throw "Ongeldige command-meta bestandsnaam: $($metaFile.Name)"
        }
        $stepId = $Matches[1]
        if (-not $metaIds.Add($stepId)) {
            throw "Dubbele command-step-ID: $stepId"
        }

        try {
            $meta = Get-Content -LiteralPath $metaFile.FullName -Raw -Encoding UTF8 |
                ConvertFrom-Json
        }
        catch {
            throw "Command-meta JSON parseert niet voor step $stepId."
        }

        foreach ($property in @(
            'StepId', 'Description', 'WorkingDirectory', 'StartTime',
            'EndTime', 'DurationMilliseconds', 'ExitCode',
            'ExpectedExitCodes', 'Expected', 'Sensitive', 'Stdout', 'Stderr'
        )) {
            Assert-ObjectProperty -Object $meta -Name $property -Context $metaFile.Name
        }
        if ([string]$meta.StepId -ne $stepId) {
            throw "StepId in meta wijkt af van bestandsnaam voor step $stepId."
        }
        if ([string]::IsNullOrWhiteSpace([string]$meta.Description) -or
            [string]::IsNullOrWhiteSpace([string]$meta.WorkingDirectory)) {
            throw "Beschrijving of werkmap ontbreekt voor step $stepId."
        }
        if (@($meta.ExpectedExitCodes).Count -eq 0) {
            throw "ExpectedExitCodes ontbreekt voor step $stepId."
        }

        $commandPath = Join-Path $RawDirectory ($stepId + '-command.txt')
        $stdoutPath = Join-Path $RawDirectory ($stepId + '-stdout.txt')
        $stderrPath = Join-Path $RawDirectory ($stepId + '-stderr.txt')
        foreach ($requiredPath in @($commandPath, $stdoutPath, $stderrPath)) {
            if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
                throw "Raw evidence quartet is incompleet voor step $stepId."
            }
        }

        foreach ($streamName in @('Stdout', 'Stderr')) {
            $streamMeta = $meta.$streamName
            foreach ($property in @('Path', 'Bytes', 'Lines', 'Sha256')) {
                Assert-ObjectProperty -Object $streamMeta -Name $property -Context "$stepId/$streamName"
            }
            $expectedName = $stepId + '-' + $streamName.ToLowerInvariant() + '.txt'
            $streamPath = if ($streamName -eq 'Stdout') { $stdoutPath } else { $stderrPath }
            $normalizedMetaPath = ([string]$streamMeta.Path).Replace('\', '/')
            if ($normalizedMetaPath -ne ('raw/' + $expectedName)) {
                throw "Streammetadatapad wijkt af voor step $stepId/$streamName."
            }
            $item = Get-Item -LiteralPath $streamPath
            if ([long]$streamMeta.Bytes -ne $item.Length) {
                throw "Streambytes wijken af voor step $stepId/$streamName."
            }
            if ([int]$streamMeta.Lines -ne (Get-LineCount -Path $streamPath)) {
                throw "Streamregels wijken af voor step $stepId/$streamName."
            }

            if ([bool]$meta.Sensitive) {
                if ([IO.File]::ReadAllText($streamPath) -ne '[REDACTED SENSITIVE STEP]' -or
                    [string]$streamMeta.Sha256 -ne '[REDACTED]') {
                    throw "Sensitive stream is niet veilig geredigeerd voor step $stepId/$streamName."
                }
            }
            else {
                $actualHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $streamPath).Hash
                if ($actualHash -ne [string]$streamMeta.Sha256) {
                    throw "Streamhash wijkt af voor step $stepId/$streamName."
                }
            }
        }

        $commandText = [IO.File]::ReadAllText($commandPath)
        if ([bool]$meta.Sensitive) {
            if ($commandText -ne '[REDACTED SENSITIVE STEP]') {
                throw "Sensitive command is niet veilig geredigeerd voor step $stepId."
            }
        }
        elseif ($commandText -ne [string]$meta.Command) {
            throw "Commandbestand en meta verschillen voor step $stepId."
        }

        if (-not [bool]$meta.Expected) {
            $unexpectedFailureCount++
        }
        elseif ([int]$meta.ExitCode -ne 0) {
            $expectedFailureCount++
        }
    }

    foreach ($suffix in @('command.txt', 'stdout.txt', 'stderr.txt')) {
        foreach ($file in @($allRawFiles | Where-Object { $_.Name -like ('*-' + $suffix) })) {
            if ($file.Name -notmatch '^(\d{3})-(command[.]txt|stdout[.]txt|stderr[.]txt)$') {
                throw "Ongeldige raw commandbestandsnaam: $($file.Name)"
            }
            if (-not $metaIds.Contains($Matches[1])) {
                throw "Raw commandbestand zonder meta: $($file.Name)"
            }
        }
    }

    foreach ($noteFile in $noteFiles) {
        if ($noteFile.Name -notmatch '^(\d{3})-note[.]md$') {
            throw "Ongeldige note-bestandsnaam: $($noteFile.Name)"
        }
        $noteId = $Matches[1]
        if (-not $noteIds.Add($noteId)) {
            throw "Dubbele note-step-ID: $noteId"
        }
        $firstLine = [IO.File]::ReadLines($noteFile.FullName) | Select-Object -First 1
        if ([string]$firstLine -notmatch ('^# Note ' + [regex]::Escape($noteId) + ' - ')) {
            throw "Note-step-ID wijkt af van bestandsnaam voor note $noteId."
        }
    }

    return [pscustomobject]@{
        CommandCount = $metaFiles.Count
        NoteCount = $noteFiles.Count
        ExpectedFailureCount = $expectedFailureCount
        UnexpectedFailureCount = $unexpectedFailureCount
    }
}

function Get-ZipEntrySha256 {
    param([Parameter(Mandatory = $true)]$Entry)

    $stream = $null
    $sha = $null
    try {
        $stream = $Entry.Open()
        $sha = [Security.Cryptography.SHA256]::Create()
        return ([BitConverter]::ToString($sha.ComputeHash($stream))).Replace('-', '')
    }
    finally {
        if ($null -ne $sha) { $sha.Dispose() }
        if ($null -ne $stream) { $stream.Dispose() }
    }
}

$runFull = [IO.Path]::GetFullPath($RunDirectory)
if (-not (Test-Path -LiteralPath $runFull -PathType Container)) {
    throw "RunDirectory does not exist: $runFull"
}

$repoRootOutput = @(& git -C $runFull rev-parse --show-toplevel 2>$null)
if ($LASTEXITCODE -ne 0 -or $repoRootOutput.Count -eq 0) {
    throw 'RunDirectory is not inside a readable Git repository.'
}
$repoRoot = [IO.Path]::GetFullPath(([string]$repoRootOutput[0]).Trim())

$runsRoot = Split-Path -Parent $runFull
$runId = Split-Path -Leaf $runFull
$zipPath = Join-Path $runsRoot ($runId + '_BUNDLE.zip')
$buildingZipPath = Join-Path $runsRoot ($runId + '_BUNDLE.building.zip')
if (Test-Path -LiteralPath $zipPath) {
    throw "Bundle already exists and will not be overwritten: $zipPath"
}
if (Test-Path -LiteralPath $buildingZipPath) {
    Remove-Item -LiteralPath $buildingZipPath -Force
}

$requiredRunFiles = @(
    '00_REQUEST.txt',
    '01_CONTEXT.md',
    'FULL_EXECUTION_LOG.md',
    'CHANGES.md',
    'FINAL_REPORT.md',
    'UPLOAD_MANIFEST.md'
)
foreach ($name in $requiredRunFiles) {
    $requiredPath = Join-Path $runFull $name
    if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
        throw "Required run file is missing: $requiredPath"
    }
}
if (-not (Test-Path -LiteralPath (Join-Path $runFull 'raw') -PathType Container)) {
    throw 'Required raw directory is missing.'
}
$rawDirectory = Join-Path $runFull 'raw'
$rawEvidence = Assert-RawEvidence -RawDirectory $rawDirectory
$noteFiles = @(Get-ChildItem -LiteralPath $rawDirectory -Filter '*-note.md' -File)
$recoveryCount = @($noteFiles | Where-Object {
    [IO.File]::ReadAllText($_.FullName) -match '(?m)^- Categorie: RECOVERY$'
}).Count

$summaryFull = if ([IO.Path]::IsPathRooted($FinalSummaryFile)) {
    [IO.Path]::GetFullPath($FinalSummaryFile)
}
else {
    [IO.Path]::GetFullPath((Join-Path $repoRoot $FinalSummaryFile))
}
if (-not (Test-Path -LiteralPath $summaryFull -PathType Leaf) -or
    (Get-Item -LiteralPath $summaryFull).Length -eq 0) {
    throw "FinalSummaryFile is missing or empty: $summaryFull"
}

$logPath = Join-Path $runFull 'FULL_EXECUTION_LOG.md'
$manifestPath = Join-Path $runFull 'UPLOAD_MANIFEST.md'
$runRelative = Get-RelativePath -BasePath $repoRoot -TargetPath $runFull
$ignoreProbeRelative = $runRelative.TrimEnd('/') + '/FULL_EXECUTION_LOG.md'
& git -C $repoRoot check-ignore -q -- $ignoreProbeRelative
$runIgnored = $LASTEXITCODE -eq 0

$previousErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
$gitStatus = @(& git -C $repoRoot status --porcelain=v1 --untracked-files=all 2>&1 |
    ForEach-Object { [string]$_ })
$gitStatusExit = $LASTEXITCODE
$diffCheck = @(& git -C $repoRoot diff --check 2>&1 |
    ForEach-Object { [string]$_ })
$diffCheckExit = $LASTEXITCODE
$ErrorActionPreference = $previousErrorActionPreference

if ($gitStatusExit -ne 0) {
    throw "git status failed with exit code $gitStatusExit."
}

$phaseText = if ($PhaseCommitHashes.Count -eq 0) {
    '- geen'
}
else {
    ($PhaseCommitHashes | ForEach-Object { '- ' + $_ }) -join [Environment]::NewLine
}
$statusText = if ($gitStatus.Count -eq 0) {
    '    schoon'
}
else {
    ($gitStatus | ForEach-Object { '    ' + $_ }) -join [Environment]::NewLine
}
$diffText = if ($diffCheck.Count -eq 0) {
    '    geen meldingen'
}
else {
    ($diffCheck | ForEach-Object { '    ' + $_ }) -join [Environment]::NewLine
}

$reviewRoot = Join-Path $runFull 'review_files'
$reviewManifestPath = Join-Path $runFull 'REVIEW_FILES_MANIFEST.md'
$reviewRootExists = Test-Path -LiteralPath $reviewRoot
$reviewManifestExists = Test-Path -LiteralPath $reviewManifestPath
if ($reviewRootExists -or $reviewManifestExists) {
    if (-not (Test-Path -LiteralPath $reviewRoot -PathType Container) -or
        -not (Test-Path -LiteralPath $reviewManifestPath -PathType Leaf)) {
        throw 'Bestaand reviewbewijs is incompleet of heeft een ongeldig bestandstype.'
    }
}
$reuseReviewEvidence = $reviewRootExists -and $reviewManifestExists

$uniquePaths = New-Object System.Collections.Generic.List[string]
$reviewCandidates = New-Object System.Collections.Generic.List[object]
$seen = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($uploadPath in $UploadPaths) {
    $candidate = if ([IO.Path]::IsPathRooted($uploadPath)) {
        [IO.Path]::GetFullPath($uploadPath)
    }
    else {
        [IO.Path]::GetFullPath((Join-Path $repoRoot $uploadPath))
    }
    if (-not (Test-IsPathWithin -ParentPath $repoRoot -CandidatePath $candidate)) {
        throw 'UploadPath buiten de repository is niet toegestaan.'
    }
    $relative = Get-RelativePath -BasePath $repoRoot -TargetPath $candidate
    $normalizedRelative = $relative.Replace('\', '/').TrimStart('/')
    if ($normalizedRelative.StartsWith('../') -or [IO.Path]::IsPathRooted($normalizedRelative)) {
        throw 'UploadPath bevat onveilige directory traversal.'
    }
    if (Test-IsForbiddenReviewFile -RelativePath $normalizedRelative) {
        throw "Verboden reviewbestand geweigerd: $normalizedRelative"
    }
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) {
        throw "UploadPath is geen gewoon bestand: $normalizedRelative"
    }
    if (-not $seen.Add($candidate)) {
        continue
    }

    $uniquePaths.Add($candidate)
    $underRun = Test-IsPathWithin -ParentPath $runFull -CandidatePath $candidate
    $underRunsRoot = $normalizedRelative -match '^docs/_codex_runs/'
    if (-not $underRun -and -not $underRunsRoot) {
        $item = Get-Item -LiteralPath $candidate
        if ($item.Length -le 0) {
            throw "Onverwacht 0-byte reviewbestand: $normalizedRelative"
        }
        $reviewCandidates.Add([pscustomobject]@{
            SourceFull = $candidate
            Relative = $normalizedRelative
            Bytes = $item.Length
            SourceHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $candidate).Hash
        })
    }
}

if ($reviewCandidates.Count -eq 0) {
    throw 'Geen repositorybestanden geselecteerd voor review_files.'
}

if (-not $reuseReviewEvidence) {
    New-Item -ItemType Directory -Path $reviewRoot | Out-Null
}
$reviewRecords = New-Object System.Collections.Generic.List[object]
foreach ($candidate in $reviewCandidates) {
    $copyPath = Join-Path $reviewRoot $candidate.Relative
    $copyFull = [IO.Path]::GetFullPath($copyPath)
    if (-not (Test-IsPathWithin -ParentPath $reviewRoot -CandidatePath $copyFull)) {
        throw "Reviewkopie valt buiten review_files: $($candidate.Relative)"
    }
    if ($reuseReviewEvidence) {
        if (-not (Test-Path -LiteralPath $copyFull -PathType Leaf)) {
            throw "Bestaande reviewkopie ontbreekt: $($candidate.Relative)"
        }
        if ((Get-Item -LiteralPath $copyFull).Length -ne $candidate.Bytes) {
            throw "Bestaande reviewkopiebytes wijken af: $($candidate.Relative)"
        }
    }
    else {
        $copyParent = Split-Path -Parent $copyFull
        if (-not (Test-Path -LiteralPath $copyParent -PathType Container)) {
            New-Item -ItemType Directory -Path $copyParent -Force | Out-Null
        }
        Copy-Item -LiteralPath $candidate.SourceFull -Destination $copyFull
    }
    $copyHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $copyFull).Hash
    if ($copyHash -ne $candidate.SourceHash) {
        throw "Reviewkopiehash wijkt af: $($candidate.Relative)"
    }
    $reviewRecords.Add([pscustomobject]@{
        SourceFull = $candidate.SourceFull
        Relative = $candidate.Relative
        Bytes = $candidate.Bytes
        SourceHash = $candidate.SourceHash
        CopyFull = $copyFull
        ReviewRelative = ('review_files/' + $candidate.Relative)
        CopyHash = $copyHash
    })
}

if ($reuseReviewEvidence) {
    $expectedCopyPaths = @($reviewRecords | ForEach-Object { $_.CopyFull } | Sort-Object)
    $actualCopyPaths = @(Get-ChildItem -LiteralPath $reviewRoot -Recurse -File |
        ForEach-Object { $_.FullName } | Sort-Object)
    if (($actualCopyPaths -join [Environment]::NewLine) -ne
        ($expectedCopyPaths -join [Environment]::NewLine)) {
        throw 'Bestaand review_files bevat ontbrekende of extra bestanden.'
    }
}

$reviewRows = @($reviewRecords | ForEach-Object {
    '| ' + $_.Relative + ' | ' + $_.SourceFull + ' | ' + $_.Bytes + ' | ' +
    $_.SourceHash + ' | ' + $_.ReviewRelative + ' | ' + $_.CopyHash + ' | ja |'
})
$reviewManifest = @"
# Review Files Manifest

| Repositorypad | Origineel volledig pad | Bytes | SHA-256 origineel | Reviewpad | SHA-256 kopie | Hashmatch |
| --- | --- | ---: | --- | --- | --- | --- |
$($reviewRows -join [Environment]::NewLine)

- Reviewbestanden: $($reviewRecords.Count)
- Alle bron-/kopiehashes gelijk: ja
- Bronnen gewijzigd door finalisatie: nee
"@
if ($reuseReviewEvidence) {
    if ([IO.File]::ReadAllText($reviewManifestPath) -ne $reviewManifest) {
        throw 'Bestaand REVIEW_FILES_MANIFEST.md wijkt af van de opnieuw gevalideerde reviewbestanden.'
    }
}
else {
    Write-Utf8NoBom -Path $reviewManifestPath -Content $reviewManifest
}

foreach ($path in @($manifestPath, $reviewManifestPath)) {
    if ($seen.Add($path)) {
        $uniquePaths.Add($path)
    }
}

$uploadRows = New-Object System.Collections.Generic.List[string]
foreach ($path in $uniquePaths) {
    if ($path -eq $manifestPath) {
        $relative = Get-RelativePath -BasePath $repoRoot -TargetPath $path
        $state = Get-UploadState -RepositoryRoot $repoRoot -RelativePath $relative
        $uploadRows.Add(
            '| ' + $relative + ' | ' + $path + ' | [SELF_REFERENCE] | ' +
            '[SELF_REFERENCE] | ' + $state + ' | ' + (Get-UploadReason $relative) + ' |'
        )
        continue
    }

    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Upload file does not exist: $path"
    }
    $relative = Get-RelativePath -BasePath $repoRoot -TargetPath $path
    $item = Get-Item -LiteralPath $path
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
    $state = Get-UploadState -RepositoryRoot $repoRoot -RelativePath $relative
    $uploadRows.Add(
        '| ' + $relative + ' | ' + $path + ' | ' + $item.Length + ' | ' +
        $hash + ' | ' + $state + ' | ' + (Get-UploadReason $relative) + ' |'
    )
}

$manifest = @"
# Upload Manifest

| Veld | Waarde |
| --- | --- |
| Taak | $TaskId |
| Status | $Status |
| Masterplan | $MasterplanVersion |
| Run-ID | $([IO.Path]::GetFileName($runFull)) |
| Runmap door Git genegeerd | $runIgnored |
| git diff --check exitcode | $diffCheckExit |
| Raw command-evidence compleet | ja |
| Commandostappen | $($rawEvidence.CommandCount) |
| Notes | $($rawEvidence.NoteCount) |
| Reviewbestanden | $($reviewRecords.Count) |
| Reviewkopiehashes gelijk | ja |

## Fasecommits

$phaseText

## Git-status

$statusText

## git diff --check

$diffText

## Uploadbestanden

| Relatief pad | Volledig Windows-pad | Bytes | SHA-256 | Git-status | Uploadreden |
| --- | --- | ---: | --- | --- | --- |
$($uploadRows -join [Environment]::NewLine)

## Zelfreferentiebeperking

Een bestand kan zijn eigen uiteindelijke SHA-256 niet in zichzelf opnemen.
De manifestregel gebruikt daarom SELF_REFERENCE. De manifesthash wordt
hieronder vastgelegd voor de snapshot direct voordat die hashregel wordt
toegevoegd. Ook kan de ZIP zijn eigen hash niet bevatten; de lokale
manifestversie na bundelvorming bevat de daadwerkelijke ZIP-hash, terwijl
de manifestkopie in de ZIP de pre-bundle snapshot is.

De standaard menselijke overdracht bestaat uit deze ene runbundle. De
repositorysnapshots staan onder `review_files/` en hun hashes staan in
`REVIEW_FILES_MANIFEST.md`.
"@

Write-Utf8NoBom -Path $manifestPath -Content $manifest
$manifestSnapshotItem = Get-Item -LiteralPath $manifestPath
$manifestSnapshotHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $manifestPath).Hash
Append-Utf8NoBom -Path $manifestPath -Content @"

## Manifest-snapshothash

- Bytes voor deze sectie: $($manifestSnapshotItem.Length)
- SHA-256 voor deze sectie: $manifestSnapshotHash
"@

$preBundleLog = @"

## Finalisatievoorcontrole

- Taak: $TaskId
- Status: $Status
- Masterplan: $MasterplanVersion
- Runmap genegeerd: $runIgnored
- git diff --check exitcode: $diffCheckExit
- Uploadpaden voor bundel: $($uniquePaths.Count)
- Raw command-evidence compleet: ja ($($rawEvidence.CommandCount) stappen)
- Notes mechanisch uniek: ja ($($rawEvidence.NoteCount) notes)
- Reviewbestanden: $($reviewRecords.Count)
- Reviewkopiehashes gelijk: ja
"@
Append-Utf8NoBom -Path $logPath -Content $preBundleLog

Add-Type -AssemblyName System.IO.Compression.FileSystem
$expectedArchiveEntries = @(Get-ChildItem -LiteralPath $runFull -Recurse -File |
    ForEach-Object {
        (Get-RelativePath -BasePath $runFull -TargetPath $_.FullName).Replace('\', '/')
    })
$entryCount = 0
$entryNames = @()
$archiveValidated = $false

try {
    Compress-Archive -Path (Join-Path $runFull '*') `
        -DestinationPath $buildingZipPath -CompressionLevel Optimal

    $archive = $null
    try {
        $archive = [IO.Compression.ZipFile]::OpenRead($buildingZipPath)
        $fileEntries = @($archive.Entries | Where-Object {
            -not [string]::IsNullOrEmpty($_.Name)
        })
        $entryNames = @($fileEntries | ForEach-Object {
            $_.FullName.Replace('\', '/')
        })
        $entryCount = $fileEntries.Count

        if ($entryCount -ne $expectedArchiveEntries.Count) {
            throw "Tijdelijke bundle heeft $entryCount bestanden; verwacht $($expectedArchiveEntries.Count)."
        }
        foreach ($expectedEntry in $expectedArchiveEntries) {
            if ($entryNames -cnotcontains $expectedEntry) {
                throw "Tijdelijke bundle mist entry: $expectedEntry"
            }
        }
        foreach ($actualEntry in $entryNames) {
            if ($expectedArchiveEntries -cnotcontains $actualEntry) {
                throw "Tijdelijke bundle bevat onverwachte entry: $actualEntry"
            }
        }
        foreach ($requiredEntry in $requiredRunFiles + @('REVIEW_FILES_MANIFEST.md')) {
            if ($entryNames -cnotcontains $requiredEntry) {
                throw "Tijdelijke bundle mist verplicht runbestand: $requiredEntry"
            }
        }
        if ($entryNames -contains [IO.Path]::GetFileName($zipPath) -or
            $entryNames -contains [IO.Path]::GetFileName($buildingZipPath)) {
            throw 'Tijdelijke bundle bevat zichzelf.'
        }

        foreach ($reviewRecord in $reviewRecords) {
            $matchingEntries = @($fileEntries | Where-Object {
                $_.FullName.Replace('\', '/') -ceq $reviewRecord.ReviewRelative
            })
            if ($matchingEntries.Count -ne 1) {
                throw "Reviewbestand ontbreekt of is dubbel in bundle: $($reviewRecord.Relative)"
            }
            if ($matchingEntries[0].Length -le 0) {
                throw "Reviewbestand is 0 bytes in bundle: $($reviewRecord.Relative)"
            }
            $archiveHash = Get-ZipEntrySha256 -Entry $matchingEntries[0]
            if ($archiveHash -ne $reviewRecord.SourceHash) {
                throw "Reviewbestandhash wijkt af in bundle: $($reviewRecord.Relative)"
            }
        }
        $archiveValidated = $true
    }
    finally {
        if ($null -ne $archive) {
            $archive.Dispose()
        }
    }

    if (-not $archiveValidated) {
        throw 'Tijdelijke bundle is niet volledig gevalideerd.'
    }
    Move-Item -LiteralPath $buildingZipPath -Destination $zipPath
}
catch {
    if (Test-Path -LiteralPath $buildingZipPath) {
        Remove-Item -LiteralPath $buildingZipPath -Force
    }
    throw
}

$zipItem = Get-Item -LiteralPath $zipPath
$zipHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $zipPath).Hash
$zipRelative = Get-RelativePath -BasePath $repoRoot -TargetPath $zipPath
$zipState = Get-UploadState -RepositoryRoot $repoRoot -RelativePath $zipRelative

Append-Utf8NoBom -Path $manifestPath -Content @"

## Runbundle

| Relatief pad | Volledig Windows-pad | Bytes | SHA-256 | Git-status | Uploadreden |
| --- | --- | ---: | --- | --- | --- |
| $zipRelative | $zipPath | $($zipItem.Length) | $zipHash | $zipState | $(Get-UploadReason $zipRelative) |

- ZIP-entrycount: $entryCount
- ZIP opent read-only: ja
- ZIP bevat zichzelf: $($entryNames -contains ([IO.Path]::GetFileName($zipPath)))
- Tijdelijke building-ZIP na promotie aanwezig: $(Test-Path -LiteralPath $buildingZipPath)
- Raw command-evidence compleet: ja
- Reviewbestanden in bundle: $($reviewRecords.Count)
- Reviewbestanden bron/kopie/bundle hashmatch: ja
- Snapshotgrens: de ZIP bevat alle runbestanden zoals zij direct voor de
  ZIP-aanmaak bestonden. De lokale manifest- en logaanvulling met de
  ZIP-hash is noodzakelijkerwijs nieuwer dan hun kopie in de ZIP.
"@

Append-Utf8NoBom -Path $logPath -Content @"

## Finalisatieresultaat

- Bundle: $zipRelative
- Bytes: $($zipItem.Length)
- SHA-256: $zipHash
- ZIP-entrycount: $entryCount
- ZIP opent read-only: ja
- Runmap genegeerd: $runIgnored
- git diff --check exitcode: $diffCheckExit
- Raw command-evidence compleet: ja
- Reviewbestanden: $($reviewRecords.Count)
- Reviewbestanden bron/kopie/bundle hashmatch: ja
- Tijdelijke building-ZIP na promotie aanwezig: $(Test-Path -LiteralPath $buildingZipPath)
- Zelfreferentiebeperking: manifest en ZIP kunnen hun eigen uiteindelijke
  hash niet in de gehashte snapshot bevatten; de lokale manifestversie
  legt de controleerbare post-bundle hash vast.
"@

Append-Utf8NoBom -Path $summaryFull -Content @"

## Post-bundle-integriteit

- Runbundle: $zipRelative
- Volledig Windows-pad: $zipPath
- ZIP-bytes: $($zipItem.Length)
- ZIP-entrycount: $entryCount
- ZIP-SHA-256: $zipHash
- ZIP opent read-only: ja
- Runmap door Git genegeerd: $runIgnored
- git diff --check exitcode tijdens finalisatie: $diffCheckExit
- Gelogde commandostappen voor finalisatie: $($rawEvidence.CommandCount)
- Gelogde notes voor finalisatie: $($rawEvidence.NoteCount)
- Verwachte niet-nulstappen: $($rawEvidence.ExpectedFailureCount)
- Onverwachte failurestappen: $($rawEvidence.UnexpectedFailureCount)
- RECOVERY-notes: $recoveryCount
- Raw command-evidence compleet: ja
- Reviewbestanden: $($reviewRecords.Count)
- Reviewbestanden bron/kopie/bundle hashmatch: ja
- Tijdelijke building-ZIP na promotie aanwezig: $(Test-Path -LiteralPath $buildingZipPath)
- Snapshotgrens: de ZIP bevat de volledige run zoals die direct voor
  bundelvorming bestond; deze post-bundle-hash kan niet in de gehashte
  ZIP-snapshot zelf staan.
"@

$success = $runIgnored -and $diffCheckExit -eq 0 -and $entryCount -gt 0 -and
    $archiveValidated -and $reviewRecords.Count -gt 0 -and
    -not (Test-Path -LiteralPath $buildingZipPath)
Write-Output (
    '[finalize] status={0} entries={1} review={2} raw={3} ignored={4} diffcheck={5}' -f
    $(if ($success) { 'ok' } else { 'failed' }),
    $entryCount,
    $reviewRecords.Count,
    $rawEvidence.CommandCount,
    $runIgnored,
    $diffCheckExit
)

if (-not $success) {
    exit 1
}
exit 0
