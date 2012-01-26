SeleniumによるテストケースをreSTで書いてみよう
===============================================

   ファイルを変換するスクリプトの作成に結構手間取ってますし、「テスト
   ケースを書いてみる」が今回の目的なので、「ファイル決め打ち」とか
   いろいろな点の作り込みは省略しています。


reSTructured Text で、テストケース書けないの?
----------------------------------------------

ということで、reSTructured Textでテストケース書いてみました。

やってみた手順書いておきますね。(そこまで単純でもないかと思うんですけど)

まずは :doc:`testcase` のようなものを書いて、それを ``rst2html`` を使って
HTMLに変換。

.. blockdiag::

   blockdiag{

      testcase_rst -> rst2html -> testcase_html; 
   }

生成された testcase.html から Selenium が扱えるようなHTML群を生成する
``selgenfiles.py`` を実行。

   
.. blockdiag::

   blockdiag{
      testcase_html -> selgenfiles_py; 
      selgenfiles_py -> TestSuite_html,google_search_blender_html,google_search_sphinx_html;
   }
   

Selenium を実行します。テストが終了すると、指定のHTMLが出力されます。
今回の場合は result.html ですね。

googletest.bat::

   java -jar C:\usr\proj\seltest\selenium-server-standalone-2.15.0.jar -htmlSuite "*firefox" "http://google.com" "C:\usr\proj\seltest\TestSuite.html" "C:\usr\proj\seltest\result.html" -timeout "60000"

.. blockdiag::

   blockdiag{
      group {
         googletest_bat; Selenium;
      }
   
      googletest_bat -> result_html;
   
   }

出力された結果ファイル result.html を resulthtmltorst.py を使って reST に変換します。


.. blockdiag::

   blockdiag{
      result_html -> resulthtmltorst_py -> result_rst;
   }

実際のファイル
----------------

実際のテストケースを記述したファイル、最終的に生成されたファイルは以下からご覧になれます。

.. toctree::
   :maxdepth: 1

   testcase
   result