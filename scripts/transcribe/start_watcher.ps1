# Double-click (or run) to start the auto-detect meeting watcher.
# Leave this window open (minimized is fine) while you work — it watches in the background and
# only records while Zoom or Teams is actually running. Ctrl+C in this window to stop.

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $ScriptDir "watch_and_record.py")

Write-Host "`nWatcher stopped. Press any key to close..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
