===================
concrete5関西 4回目
===================

はじまりましたー
----------------

Concrete5

   日本語進捗報告

   5.4.2.2 -> リリース

      http://concrete5-japan.org/

   バグ&セキュリティの更新

5.4.2.2のアップグレードについて
-------------------------------

バックアップがうまくいかない→タイムアウト
   * サーバーカウボーイ
   * バーガーキング
   * ロリポップも？
      * インストールも結構厳しかった(1-2年前)
      * 一気にインストールする
      * DBがよくなったのか最近はうまくいっている様子
   * さくら５００MB
   * レオサーバー
   * CPI

データベースをコンパクトにすることで対応

ページ閲覧ログは大量のデータを取得する

   * これが原因でアップグレードがうまくいかないことも

DB管理ツールとか使った方がいい

   PHPmyadmin

Page Statistics のテーブルを「空にする」 

アップデート
---------------

「アップデートをダウンロード」から

実演:

インポート

バックアップを戻せばすぐに5.4.1.1の環境に戻せます

.. note::

   アップグレードから戻したい場合の方法はconcrete5の日本語公式ページにやり方が載っています。

「予期せぬエラーが発生しました」

   アップグレード後にキャッシュをクリアしておく

      * concrete5のキャッシュ
      * ブラウザのキャッシュ

後半
====

興味のあることピックアップ
--------------------------

      * コンポーザー
      * Open ID
      * アドオンおすすめ
      * CSS
      * jQuery
      * Jimdoとの違い
      * アドミンバーが出ない
      * 下書き保存時のスペース設定が消える
      * 共通パーツの扱い
         * Global area Add-on

Composerの使い方
================

「コンポーザー」は事前準備が必要。

   「コンポーザーで選択可能にしますか？」にチェック。

   .. tip ::

      コンポーザーのデフォルトでは最小限の入力項目しか無いので、
      入力項目を追加する必要があります。

         コンポーザー設定

ページタイプで選んだページのブロックで、コンポーザーの編集対象とすることで
コンポーザーで編集出来る入力項目が

   同じフォーマットでどんどん書いていくときに使える機能

   .. note ::
   
      ベータ版

   ::

      必須とか判断しないんですか？

   ::

      無いと思います。


   * Compoeser草稿が自動保存される&リストに出てくるのでイイ

Open ID
-------

標準機能でOpenIDをサポート。

   * 「ログイン&ユーザー登録」→ 「OpenIDを使用する」

      * yahooはいけました？？？

   * Twitter Loginというものが公開されている
   
      * 入れてみた→ん？ん？→追加調査が必要

JimdoとConcrete5の違い
-----------------------

この最近「みんビズ」とConcrete5 の違いって何？のお話がきてます。

   * みんなのビジネスオンライン
      * http://www.minbiz.jp/
   * みんビズ作って１年無料
      * 次年度からお金かかりますよ

concrete5はページタイプCMS

   いろいろできるけれど

Jimdoは簡単に見える

   制限や拡張がおおい

ドメインの話

   みんビスで独自ドメイン付きで契約するよりも「最初に独自ドメイン」を
   取っておくことをおすすめ

   .. tip ::

      あとで何か拡張するときを考えましょうね。

ショップカート

   * Pro版 25個
   * プラス2,980円で無制限

何が違うねん？
--------------

   * 簡単に構築出来る→みんビズ
   * 自由度が高いけど勉強してね→Concrete5

   .. tip:

      拡張性なども含めて考えましょう。

その他
------

みんビズの連携団体

   * google
   * KDDI
   * Jimdo
   * 中小機構
   * ITコーディネータ協会

たくさんのサイトが(万単位)出来ているという。

