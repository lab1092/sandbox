
rem mkdocsrst.py

rem mkressrst.py


rem mk_ars_tabledef.py >ars_tabledef.rst

call .\make.bat clean

call .\make.bat pdf

.\_build\pdf\sandbox.pdf
