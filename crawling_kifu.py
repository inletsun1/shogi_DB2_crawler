from urllib.request import urlopen
import re
import time
import requests
from selenium import webdriver
import os

#url = 'https://shogidb2.com/strategy/%E7%9F%A2%E5%80%89/page/'
url = 'https://shogidb2.com/strategy/%E7%9F%A2%E5%80%89/page/'
strategy_name = "矢倉"
pages = 2
driver = webdriver.PhantomJS()
print("Driver opened.")

def crawl_kifu_url(url, dpt):
    if dpt<1:
        pass
    else:
        k = 0
        for i in range(1, dpt+1):
            kifu_urls = get_kifu_url(url + str(i))
            print("Depth: " + str(i))
            for kifu_url in kifu_urls:
                k += 1
                kifu, filename = crawl_raw_kifu(kifu_url)
                time.sleep(5)
                writecsa(kifu, filename)
                print("Wrote "+filename)
        print("Finished!")
            

def get_kifu_url(url):
    global driver
    driver.get(url)
    kifus = driver.find_elements_by_class_name('list-group-item')
    kifu_urls = [a.get_attribute('href') for a in kifus] 
    return kifu_urls

def crawl_raw_kifu(url):
    f = urlopen(url)
    encoding = 'utf-8'
    text = f.read().decode(encoding)
    moves = re.search(r'\"moves\":\[.*\]', text)
    title = re.search(r'\"tournament_detail\":.*\"tournament\"', text)
    title = title.group(0)
    title = title.split(",")
    title = title[0]
    title = title.split(":")
    title = title[1][1:-1]

    player1 = re.search(r'\"player1\":.*\"place\"', text)
    player2 = re.search(r'\"player2\":.*\"player1\"', text)
    player1 = player1.group(0)
    player1 = player1.split(",")
    player1 = player1[0]
    player1 = player1.split(":")
    player1 = player1[1][1:-1]

    player2 = player2.group(0)
    player2 = player2.split(",")
    player2 = player2[0]
    player2 = player2.split(":")
    player2 = player2[1][1:-1]

    filename = title + "_" + player1 + "_" + player2 + ".csa"
    kifu = [m.group(1) for m in re.finditer(r'\"csa\":\"(.*?)\",', moves.group(0))]
    return kifu, filename

def writecsa(kifu, filename):
    print("write " + filename)
    mkdir('./棋譜')
    mkdir('./棋譜/' + strategy_name)
    with open('./棋譜/' + strategy_name + '/' +filename, 'w') as f:
        #csaファイル形式のバージョン
        version = 'V2.2\n'
        #開始局面の設定
        HIRATE = 'P1-KY-KE-GI-KI-OU-KI-GI-KE-KY\nP2 * -HI *  *  *  *  * -KA * \nP3-FU-FU-FU-FU-FU-FU-FU-FU-FU\nP4 *  *  *  *  *  *  *  *  * \nP5 *  *  *  *  *  *  *  *  * \nP6 *  *  *  *  *  *  *  *  * \nP7+FU+FU+FU+FU+FU+FU+FU+FU+FU\nP8 * +KA *  *  *  *  * +HI * \nP9+KY+KE+GI+KI+OU+KI+GI+KE+KY\n'
        f.write(version)
        f.write(HIRATE)
        f.write('\'sashite\n')
        for i in range(len(kifu)):
            f.write(kifu[i]+'\n')
   
#url = 'https://shogidb2.com/games/ed9f7e5bb50c64376e49aee4dd30deec194a4618'
#url = 'https://shogidb2.com/strategies'

def mkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

crawl_kifu_url(url, pages)
