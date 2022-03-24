@echo off
set /p namef="Enter Name of file for decryption: "
mkdir "%~dp0\%namef%\"
cd "%~dp0\%namef%\"
py "%~dp0dec3.py" "%~dp0%namef%.list" "%~dp0%namef%.pack"
pause