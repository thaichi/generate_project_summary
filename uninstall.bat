@echo off
setlocal enabledelayedexpansion

echo Uninstalling generate_project_summary...

:: スクリプトのディレクトリを取得
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

:: ユーザーに確認
echo This will remove the generate_project_summary directory and its entry from PATH.
echo Are you sure you want to proceed? (Y/N)
set /p CONFIRM=
if /i "%CONFIRM%" neq "Y" (
    echo Uninstall cancelled.
    goto :EOF
)

:: ユーザーのPATHから削除
for /f "tokens=2*" %%A in ('reg query "HKCU\Environment" /v PATH') do set "userpath=%%B"
set "newpath=!userpath:%SCRIPT_DIR%;=!"
setx PATH "%newpath%"
if !errorlevel! neq 0 (
    echo Failed to update PATH. Please update it manually.
    pause
)

:: ディレクトリの削除
cd ..
if exist "%SCRIPT_DIR%" (
    rmdir /s /q "%SCRIPT_DIR%"
    if !errorlevel! neq 0 (
        echo Failed to remove the directory. Please delete it manually.
        pause
    ) else (
        echo Directory removed successfully.
    )
)

echo Uninstallation complete.
echo Please restart your command prompt for the changes to take effect.

pause