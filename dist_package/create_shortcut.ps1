# create_shortcut.ps1

$targetPath = "$PSScriptRoot\launcher.bat"
$resolvedTargetPath = (Resolve-Path $targetPath).Path
$shortcutPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath("Desktop"), "MPScrubber.lnk")
$shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut($shortcutPath)
$shortcut.TargetPath = $resolvedTargetPath
$shortcut.Save()