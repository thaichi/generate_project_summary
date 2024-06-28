@echo off
setlocal enabledelayedexpansion

echo Setting up generate_project_summary...

:: スクリプトのディレクトリを取得
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

:: ユーザーのPATHを取得
for /f "tokens=2*" %%A in ('reg query "HKCU\Environment" /v PATH') do set "userpath=%%B"

:: スクリプトのディレクトリがユーザーのPATHに含まれているか確認
echo !userpath! | findstr /C:"%SCRIPT_DIR%" >nul
if !errorlevel! neq 0 (
    :: ユーザーのPATHに追加
    if defined userpath (
        setx PATH "%userpath%;%SCRIPT_DIR%"
    ) else (
        setx PATH "%SCRIPT_DIR%"
    )
    if !errorlevel! neq 0 (
        echo Failed to update PATH. Please check your permissions.
        pause
        exit /b 1
    )
    echo Added %SCRIPT_DIR% to user PATH.
) else (
    echo %SCRIPT_DIR% is already in user PATH.
)

:: generate_project_summary.batファイルを作成
echo @echo off > "%SCRIPT_DIR%\generate_project_summary.bat"
echo set PYTHONPATH=%%PYTHONPATH%%;%SCRIPT_DIR% >> "%SCRIPT_DIR%\generate_project_summary.bat"
echo python "%SCRIPT_DIR%\generate_project_summary\main.py" %%* >> "%SCRIPT_DIR%\generate_project_summary.bat"

echo Setup complete. You can now use 'generate_project_summary' command from any directory.
echo Please restart your command prompt or open a new one for the changes to take effect.

pause