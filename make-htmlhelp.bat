
call .\make.bat htmlhelp

rem 日本語ヘルプ作成のために実行

_cv_iso10646h.py
_cv_hhc.py
_cv_hhp.py

del conf.pyc
echo 日本語ヘルプのための変換が終わりました。

pause
