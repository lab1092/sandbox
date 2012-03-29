==================================================================
literalinclude ディレクティブでハイライトが有効にならない
==================================================================

   :TicketNo.: 414
   :topic: "literalinclude" directive is not highlighting files with cr-lf
   :URL: https://bitbucket.org/birkenfeld/sphinx/issue/414/literalinclude-directive-is-not
   :status: on hold


再現しよう
---------------

以下の3つを用意してみました。結果はいかに?

* 改行を **CR** で指定して保存した、hello_cr.py
* 改行を **LF** で指定して保存した、hello_lf.py
* 改行を **CRLF** で指定して保存した、hello_crlf.py


CR:

.. literalinclude:: hello_cr.py

LF:

.. literalinclude:: hello_lf.py

CRLF:

.. literalinclude:: hello_crlf.py


Sphinx 1.1.2 でmakeしてみたよ
------------------------------

Sphinx 1.1.2 でmakeしてみた結果は、以下の通り。

.. list-table::

   * - hello_cr.py
     - OK
   * - hello_lf.py
     - OK
   * - hello_crlf.py
     - NG
