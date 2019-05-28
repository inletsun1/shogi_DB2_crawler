# shogi_DB2_crawler
将棋棋譜データベースサイトである[将棋DB2](https://shogidb2.com/)から戦型別に棋譜をダウンロードするツールです。
保存形式は全て[csaファイル形式](http://www2.computer-shogi.org/protocol/record_v22.html)です。

## 使用方法
crawling_kifu.pyのurl、strategy_name、pagesの3つの変数を指定します。  
  
urlには、https://shogidb2.com/strategiesの中からダウンロードしたい戦型のurlを選択します。  
例えば矢倉をダウンロードしたければ  
url = https://shogidb2.com/strategy/矢倉/page/  
とします。  
  
strategy_nameには、ダウンロードした戦型を保存するディレクトリ名を指定します。  
  
pagesには、ダウンロードする戦型の棋譜を記載したURLページのページ数をいくつまでにするかを指定します。
例えば、url = https://shogidb2.com/strategy/矢倉/page/  
において  
pages = 4  
としたときは、page1からpage4までの4ページ分の棋譜をダウンロードします。
