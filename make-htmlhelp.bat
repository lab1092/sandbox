
call .\make.bat htmlhelp

rem 日本語ヘルプ作成のために実行

c:\python26\python.exe _cv_iso10646h.py
c:\python26\python.exe _cv_hhc.py
c:\python26\python.exe _cv_hhp.py

del conf.pyc
echo 日本語ヘルプのための変換が終わりました。

pause
