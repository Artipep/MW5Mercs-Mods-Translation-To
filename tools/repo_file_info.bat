@echo off
chcp 65001 >nul 2>&1
title Repository File Info Generator

cd /d "%~dp0"
python repo_file_info.py %*
if errorlevel 1 (
    echo.
    echo Error occurred. Exit code: %errorlevel%
    pause
)
