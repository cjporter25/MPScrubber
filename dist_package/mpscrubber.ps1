# mpscrubber.ps1

# WHY THIS LINE IS NECESSARY, ABSOLUTELY BLOWS MY MIND BUT IT IS FOR A SHORTCUT TO MAKE THIS WORK
Set-Location -Path $PSScriptRoot


# Activate the virtual environment
try {
    . "$PSScriptRoot\.venv\Scripts\Activate.ps1"
} catch {
    Write-Error "Failed to activate virtual environment. Error: $_"
    Read-Host -Prompt "Press Enter to exit"
    exit 1
}

# Run the application using python.exe so a debugging/prompt window can appear
try {
    & "$PSScriptRoot\.venv\Scripts\python.exe" "$PSScriptRoot\main.py"
} catch {
    Write-Error "Failed to start the process. Error: $_"
    Read-Host -Prompt "Press Enter to exit"
    exit 1
}

# Pause to keep the window open
Read-Host -Prompt "Press Enter to exit"