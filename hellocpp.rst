========================================
C++シンタックスハイライト出力
========================================


pygmentsを使って
===================

何がうれしい?
-----------------------------

   * ソースコードのシンタックスハイライトを実現します。
   * C,C++,Python他。
   * rst -> rst2pdf でPDFファイルに変換可能。
   * Python 2.6 環境で動いています。

ソースコード(hello.cpp)
-----------------------------

標準出力に"Hello"を出力するプログラムです。

.. code-block:: cpp


   //hello.cpp
   #include <iostream>
   using namespace std;
   
   int main()
   {
       cout << "hello" << endl;
   }

行番号付きソースコード(hello.cpp)
----------------------------------

標準出力に"Hello"を出力するプログラムです。

.. code-block:: cpp
   :linenos:


   //hello.cpp
   #include <iostream>
   using namespace std;
   
   int main()
   {
       cout << "hello" << endl;
   }


