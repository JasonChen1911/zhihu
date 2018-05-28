#coding=utf8
import requests
from bs4 import BeautifulSoup
import MySQLdb as mdb
import time


def getweb(url):
    try:
        headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        }
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error:status is ", r.raise_for_status)


def Soup(url, n, m):
    html=getweb(url+str(n))
    r_soup=BeautifulSoup(html, 'lxml')
    nav_num= r_soup.body.contents[1].find_all("div",{"id":"listnav"})[0].find_all("a")[-1].text
    tr_text = r_soup.body.contents[1].find_all("tbody")[0].find_all("tr")#.find_all("td")
    for item in tr_text:
        ip=item.find("td", {"data-title":"IP"}).text
        port=item.find("td", {"data-title":"PORT"}).text
        type=item.find("td", {"data-title":"类型"}).text
        print(str(m)+" : "+type+":"+ip+":"+str(port))
        m+=1
        if m>50:
            return 0
    n+=1
    time.sleep(2)
    if n==int(nav_num)+1:
        return 0
    Soup(url, n, m)




def main():
    urls=['https://www.kuaidaili.com/free/inha/', 'http://www.xicidaili.com/nn/']
    Soup(urls[0],1,1)
if __name__ == '__main__':
    main()