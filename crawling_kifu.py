from urllib.request import urlopen
import re
import time
import requests
from selenium import webdriver

url = 'https://shogidb2.com/strategy/%E7%9F%A2%E5%80%89/page/'
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
                kifu = crawl_raw_kifu(kifu_url)
                time.sleep(0.5)
                writecsa(kifu, "test"+str(k))
                print("Wrote test"+str(k)+".csa")
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
    kifu = [m.group(1) for m in re.finditer(r'\"csa\":\"(.*?)\",', moves.group(0))]
    return kifu

def writecsa(kifu, filename):
    with open('./kifu/'+filename+'.csa', 'w') as f:
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

crawl_kifu_url(url, 2)
