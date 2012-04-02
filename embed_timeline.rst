=========================
タイムラインをembedする
=========================

Twitter
---------------

::

   .. raw:: html
   
      <div align="center">
        埋め込むコード
      </div>
      
      
.. raw:: html

   <div align="center">
   <script charset="utf-8" src="http://widgets.twimg.com/j/2/widget.js"></script>
   <script>
   new TWTR.Widget({
     version: 2,
     type: 'search',
     search: 'blender lang:ja',
     interval: 30000,
     title: 'blender',
     subject: 'nipponn no blender',
     width: 250,
     height: 300,
     theme: {
       shell: {
         background: '#fc7f3c',
         color: '#ffffff'
    },
       tweets: {
         background: '#ffffff',
         color: '#444444',
         links: '#1985b5'
       }
        },
     features: {
       scrollbar: false,
       loop: true,
       live: true,
       behavior: 'default'
     }
   }).render().start();
   </script>
   </div>
   
サイドバーに組み込む
--------------------

思ったよりも簡単でしたｗ

1. _templates フォルダに twitterembedded.html を配置。Twitter埋め込みの幅は "width: 200" と指定してみた。


::

   {% block twittertl %}
      <div>
        埋め込むコード
      </div>
   {% endblock %}


2. conf.pyの html_sidebars に、以下を指定してみる

::

   html_sidebars = {'**' : ['localtoc.html', 'relations.html', 'sourcelink.html','twitterembedded.html']}


3. make clean , make html してみる

   * http://dl.dropbox.com/u/3864210/embed_timeline.html


おおおおーっ。

ロゴを導入
----------

ロゴ画像を用意して、左のナビゲーションの上側に。180 pix 幅くらいかな。

.. code-block:: python

   html_logo = 'image/hoge.jpg'

ついでにサイドバーなどの色も変えよう
-------------------------------------

_static/default.css が無いことを確認ののち、

conf.py で使用しているテーマを確認。

.. code-block:: python

   html_theme = 'default'

``C:\Python26\Lib\site-packages\Sphinx-1.1.2-py2.6.egg\sphinx\themes\default\theme.conf``で設定できる識別子を確認。

::

   footerbgcolor    = #11303d
   footertextcolor  = #ffffff
   sidebarbgcolor   = #1c4e63
   sidebarbtncolor  = #3c6e83
   sidebartextcolor = #ffffff
   sidebarlinkcolor = #98dbcc
   relbarbgcolor    = #133f52
   relbartextcolor  = #ffffff
   relbarlinkcolor  = #ffffff
   bgcolor          = #ffffff
   textcolor        = #000000
   headbgcolor      = #f2f2f2
   headtextcolor    = #20435c
   headlinkcolor    = #c60f0f
   linkcolor        = #355f7c
   visitedlinkcolor = #355f7c
   codebgcolor      = #eeffcc
   codetextcolor    = #333333


conf.py に以下のように指定してみる(某FaceBookの色ですね)

::

   html_theme_options = {
     'footerbgcolor': '#1F4189',
     'sidebarbgcolor': '#3b5998',
     'relbarbgcolor' : '#1F4189'
   }

``make clean`` ``make html`` してみる。

