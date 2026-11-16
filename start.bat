@echo off
echo ==================================================================
echo   Starting RxR Multilingual VLN Agent Studio...
echo ==================================================================

where node >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Starting server with Node.js...
    node server.js
    goto end
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Starting server with Python...
    python main.py
    goto end
)

echo [ERROR] Neither Node.js nor Python was found on your PATH.
pause

:end
