# Define the path to the PowerShell script
$targetPath = "$PSScriptRoot\launcher.bat"

# Define the path to the batch file (optional, if you want the shortcut to point to the batch file instead)
#$targetPath = "$PSScriptRoot\run_application.bat"

# Define the shortcut path on the desktop
$shortcutPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), 'MPScrubber.lnk')

# Create a WScript.Shell COM object
$WScriptShell = New-Object -ComObject WScript.Shell

# Create the shortcut
$shortcut = $WScriptShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $targetPath
$shortcut.WorkingDirectory = $PSScriptRoot
$shortcut.Save()

Write-Output "Shortcut created on the desktop: $shortcutPath"