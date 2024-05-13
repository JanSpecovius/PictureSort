@echo off
REM Pfad zur Python-Installation
set PYTHON_PATH=Path/to/python.exe
REM Pfad zum Python-Skript
set SCRIPT_PATH=sort_pictures.py

REM Führe das Python-Skript aus
"%PYTHON_PATH%" "%SCRIPT_PATH%"

REM Halte das Fenster offen, damit du die Ausgabe sehen kannst
pause