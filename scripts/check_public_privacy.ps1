$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$tracked = @(git -C $projectRoot ls-files)
$untracked = @(git -C $projectRoot ls-files --others --exclude-standard)
$candidates = @($tracked + $untracked | Sort-Object -Unique)
$blocked = $candidates | Where-Object {
    ($_ -notmatch '^(private|raw)/README\.md$') -and
    ($_ -match '(^|/)(private|raw)/|(^|/)(coordinate|coordinates|farm|azienda|clinical|patient|sample_id|genome|assembly)([^/]*$|/)') -and
    ($_ -notmatch '^metadata/PUBLIC_RESTRICTED_POLICY\.md$')
}
if ($blocked.Count -gt 0) { Write-Error ('File non pubblicabili candidati a Git:`n' + ($blocked -join "`n")) }
Write-Output "OK: $($candidates.Count) file candidati ($($tracked.Count) tracciati, $($untracked.Count) non tracciati) senza percorsi sensibili rilevati."
