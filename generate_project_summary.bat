@echo off
set PYTHONPATH=%PYTHONPATH%;C:\Scripts\generate_project_summary
python %~dp0generate_project_summary\main.py %*