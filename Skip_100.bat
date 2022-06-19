@echo off

set /p folder=type in the Sym job URL:
python Skip_100.py --path=%folder%
pause