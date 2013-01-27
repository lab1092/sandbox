.. WordBench神戸 18回

=====================
WordBench神戸 18回
=====================

めもめもー


.. code-block:: php

   if ( ! isset( $content_width ) )
   $content_width = 625;


.. code-block:: php

   add_theme_support('post-formats')

.. code-block:: php

   add_theme_support('post-thumbnails')
   set_thumbnail_size( 624,9999) // 


.. code-block:: php

    add_action( 'after_setup_them', 'twentytwelve_setup')


customheader.php をインクルード

.. code-block:: php

    XXX


function twentytwelve_scripts_styles()
======================================

   * wp enqueue_script

     jsを読み込みます

   * wp enqueue_style

     CSSを読み込みます

直接ヘッダ部分にjsやCSSのファイルを書く方法より上記を使う事が

Why?

   * jQueryUI など 依存関係が強いものの読み込み込み順を明確に出来る
   * プラグインなど外部から操作出来る


.. code-block:: php

   wp_enqueue_style('twentytwelve-style',get_stylesheet_uri())


function twentytwelve_wp_title()
======================================

タイトルを出力するよ。

.. code-block:: php

    <title></title>


function twentytwelve_page_menu_args( $args )
===============================================
