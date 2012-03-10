rem ### Make them All ###

call make clean

rem HTML
rem ####

call make html
xcopy _build\html\*.* "%USERPROFILE%\Documents\My Dropbox\Public\" /A /Y

rem HTMLHELP(.chm)
rem ##############

call make htmlhelp

c:\python26\python.exe _cv_iso10646h.py
c:\python26\python.exe _cv_hhc.py
c:\python26\python.exe _cv_hhp.py

rem Compile to CHM

"C:\Program Files\HTML Help Workshop\hhc.exe" _build\htmlhelp\sandboxdoc.hhp

copy _build\htmlhelp\sandboxdoc.chm "%USERPROFILE%\Documents\My Dropbox\Public\"


rem singlehtml to PDF
rem #################

sphinx-build -b singlehtml -c _ext -d _build/doctree . _build/singlehtml

rem make PDF file to dropbox directory
"C:\Program Files\wkhtmltopdf\wkhtmltopdf.exe" _build/singlehtml/index.html "%USERPROFILE%\Documents\My Dropbox\Public\index.pdf"

