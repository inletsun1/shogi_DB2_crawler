# shogi_DB2_crawler
将棋棋譜データベースサイトである[将棋DB2](https://shogidb2.com/)から戦型別に棋譜をダウンロードするツールです。
保存形式は全て[csaファイル形式](http://www2.computer-shogi.org/protocol/record_v22.html)です。

##確認した動作環境
Windows Subsytems for windows Ubuntu18.04
Python3.7.3

##使用するまでの準備
Pythonのインストール(3.7.xを推奨)
https://www.python.org/downloads/

pipにより以下のパッケージをインストールする
requests(https://requests-docs-ja.readthedocs.io/en/latest/user/install/#install)
seleinum(https://pypi.org/project/selenium/)

Google Chormeのインストール
https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=ja
インストールしたGoogle Chromeのバージョンに対応したChrome driverのインストールし、解凍。適当なフォルダに保存する
https://chromedriver.chromium.org/downloads

crawling_kifu.pyファイルの22行目driver = webdriver.Chrome()のexecutable_pathの引数に、chromedriverの保存先ディレクトリを入力。

## 使用方法
crawling_kifu.pyをコマンドプロンプトやターミナルなどお好みの環境で実行。
  
インストール先のURLを聞かれるので
https://shogidb2.com/strategies
の中からダウンロードしたい戦型のurlを選択します。  
例えば四間飛車をダウンロードしたければ  
url = https://shogidb2.com/strategy/四間飛車  
とします。  
  
次に、分類したい戦法名を聞かれるので戦法名を入力します。これは棋譜を保存するフォルダ名になるのでお好みの名前をつけて良いです。  

最後に、保存するページ数を指定します。
例えば、url = https://shogidb2.com/strategy/四間飛車  
において  
pages = 4  
としたときは、https://shogidb2.com/strategy/四間飛車　からhttps://shogidb2.com/strategy/四間飛車/page/4　までの4ページ分の棋譜をダウンロードします。
