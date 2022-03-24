@echo off
set /p namef="Enter folder name(same directory): "
py "%~dp0doublegen.py" "%~dp0\%namef%" "%namef%"
pause