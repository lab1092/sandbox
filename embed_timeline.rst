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
      <div align="center">
        埋め込むコード
      </div>
   {% endblock %}


2. conf.pyの html_sidebars に、以下を指定してみる

::

   html_sidebars = {'**' : ['localtoc.html', 'relations.html', 'sourcelink.html','twitterembedded.html']}


3. make clean , make html してみる

   * http://dl.dropbox.com/u/3864210/embed_timeline.html


おおおおーっ。