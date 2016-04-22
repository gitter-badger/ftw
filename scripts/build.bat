if exist build rd /s /q build
if exist dist rd /s /q dist
pyinstaller ftw.py
if exist build rd /s /q build
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::CreateFromDirectory('dist/ftw', 'ftw-for-windows.zip'); }"
