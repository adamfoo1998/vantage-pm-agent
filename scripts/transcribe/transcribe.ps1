# Drag-and-drop wrapper for transcribe.py.
# Usage: drag an audio file (m4a/mp3/wav/mp4) onto this script in Explorer,
# or run: .\transcribe.ps1 "path\to\recording.m4a" "meeting-name"

param(
    [Parameter(Mandatory = $true)][string]$AudioFile,
    [string]$MeetingName
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "transcribe.py"

if (-not (Test-Path $AudioFile)) {
    Write-Error "Audio file not found: $AudioFile"
    exit 1
}

if ($MeetingName) {
    python $PythonScript $AudioFile $MeetingName
} else {
    python $PythonScript $AudioFile
}

Write-Host "`nDone. Press any key to close..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
