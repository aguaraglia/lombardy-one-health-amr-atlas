$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$tracked = @(git -C $projectRoot ls-files)
$blocked = $tracked | Where-Object {
    ($_ -notmatch '^(private|raw)/README\.md$') -and
    ($_ -match '(^|/)(private|raw)/|(^|/)(coordinate|coordinates|farm|azienda|clinical|patient|sample_id|genome|assembly)([^/]*$|/)') -and
    ($_ -notmatch '^metadata/PUBLIC_RESTRICTED_POLICY\.md$')
}
if ($blocked.Count -gt 0) { Write-Error ('File non pubblicabili tracciati da Git:`n' + ($blocked -join "`n")) }
Write-Output "OK: $($tracked.Count) file tracciati senza percorsi sensibili rilevati."


