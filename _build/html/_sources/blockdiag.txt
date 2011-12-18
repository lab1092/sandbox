
===========================
blockdiagの表示も出来るよ!! 
===========================

インタラクティブなblockdiagもあるよ。

   http://interactive.blockdiag.com/

こんな画が書けるよ!!

.. blockdiag ::

   diagram {
      // Set labels to nodes.
      A [label = "Sphinx"];
      B [label = "blockdiag"];
      C [label = "とかとか"];

      // Set labels to edges. (short text only)
      A -> C ;
      B -> C
   }


Tips for win
===========================

conf.py にフォントファイルのパスを追記。

.. code-block:: python

   # Fontpath for blockdiag (truetype font)
   blockdiag_fontpath = r'c:\usr\fonts\MigMix-1P-bold.ttf'
   
   # Fontpath for blockdiag (truetype font)
   nwdiag_fontpath = r'c:\usr\fonts\MigMix-1P-bold.ttf'


フォントファイルは今回MigMixを使いました。

   http://mix-mplus-ipa.sourceforge.jp/migmix/

Python Imaging Library (PIL)サイトのWindowsのバイナリを
インストールして使う場合には、バージョン 1.1.6 を選びましょう。
FreeType2サポートが1.1.7には組み込まれていないとか。

   http://www.pythonware.com/products/pil/



