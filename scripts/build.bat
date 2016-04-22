if exist build rd /s /q build
if exist dist rd /s /q dist
if exist ftw.spec del ftw.spec
pyinstaller ftw.py
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::CreateFromDirectory('dist/ftw', 'ftw-for-windows.zip'); }"
if exist build rd /s /q build
if exist dist rd /s /q dist
if exist ftw.spec del ftw.spec
