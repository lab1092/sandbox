@echo off
for /f %%R in ('dir /b *.rst ') do call :1 %%R
goto :eof

:1
call rst2pdfc.bat %1 docs/output/%1.pdf



