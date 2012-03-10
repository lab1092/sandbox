sphinx-build -b singlehtml -c _ext -d _build/doctree . _build/singlehtml

rem make PDF file to dropbox directory
"C:\Program Files\wkhtmltopdf\wkhtmltopdf.exe" _build/singlehtml/index.html "%USERPROFILE%\Documents\My Dropbox\Public\index.pdf"

