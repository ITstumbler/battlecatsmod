@echo off
set /p namef="Enter old folder(same directory): "
set /p namec="Enter new folder(same directory): "
py "%~dp0checkdifferencewithnewfiles.py" "%~dp0\%namef%" "%~dp0\%namec%"
pause