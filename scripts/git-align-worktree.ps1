# Veilig lokaal Git main gelijkzetten aan origin/main.
# Verwijdert/stasht NIETS. Geen reset, clean, force of live theme push.
# Gebruik: powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\git-align-worktree.ps1
[CmdletBinding()]
param([switch]$CheckOnly)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location -LiteralPath $root
Write-Host "Git map: $root"

function RunGit {
  param([Parameter(Mandatory=$true)][string[]]$GitArgs)
  & git @GitArgs
  if ($LASTEXITCODE -ne 0) {
    throw "git $($GitArgs -join ' ') faalde met exitcode $LASTEXITCODE."
  }
}

$gitRoot = & git rev-parse --show-toplevel 2>$null
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($gitRoot)) {
  throw 'Geen Git repository in deze map. Controleer het juiste lokale BadkamerCity-project.'
}
$remote = & git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0 -or $remote -notmatch '(^|[:/])jlamping1997/badkamercity(\.git)?$') {
  throw "Onjuiste origin ($remote). Er is niets veranderd."
}
$branch = & git branch --show-current
if ($LASTEXITCODE -ne 0 -or $branch -ne 'main') {
  throw "Branch '$branch' is niet main. Er is niets veranderd."
}
$changes = @(& git status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0) { throw 'Kan lokale Git status niet lezen.' }
if ($changes.Count -gt 0) {
  Write-Warning "Working tree bevat $($changes.Count) wijzigingen. Er wordt niets weggegooid of ge-pulld."
  $changes | ForEach-Object { Write-Host $_ }
  Write-Host 'Maak eerst bewust een checkpointcommit of stash. Lees docs/AI_HANDOFF_CURRENT.md.'
  exit 2
}
Write-Host 'Startstatus: schoon.'
RunGit -GitArgs @('fetch','origin')
if (-not $CheckOnly) {
  RunGit -GitArgs @('pull','--ff-only','origin','main')
}
RunGit -GitArgs @('log','-1','--oneline')
$remaining = @(& git status --porcelain=v1 --untracked-files=all)
if ($LASTEXITCODE -ne 0) { throw 'Kan eindstatus niet lezen.' }
if ($remaining.Count -ne 0) {
  Write-Warning 'Er zijn na synchronisatie onverwacht wijzigingen; geen bestanden verwijderd.'
  $remaining | ForEach-Object { Write-Host $_ }
  exit 3
}
Write-Host 'OK: de lokale Git working tree is schoon.'
