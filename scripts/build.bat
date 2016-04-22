if exist build rd /s /q build
if exist dist rd /s /q dist
pyinstaller ftw.py
if exist build rd /s /q build
