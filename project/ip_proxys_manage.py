#coding=utf8
import requests
from bs4 import BeautifulSoup
import MySQLdb as mdb
import time
import methodOfDatabases as mod
import databases


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

def is_validity(protocol, ip, port):
    host = protocol + "://" + ip + ":" + str(port)
    hosts = {protocol: host}
    #url = "http://ip.chinaz.com/getip.aspx"
    url = 'https://www.baidu.com/'
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    }
    try:
        html = requests.get(url, headers=headers, proxies=hosts, timeout=10)
        if html.status_code == 200:
            return True
        else:
            return False
    except:
        return 'error'

#快代理解析
def kuaidlSoup(url, n, m):
    html=getweb(url+str(n))
    r_soup=BeautifulSoup(html, 'lxml')
    nav_num= r_soup.body.contents[1].find_all("div",{"id":"listnav"})[0].find_all("a")[-1].text
    tr_text = r_soup.body.contents[1].find_all("tbody")[0].find_all("tr")#.find_all("td")
    for item in tr_text:
        ip=item.find("td", {"data-title":"IP"}).text
        port=item.find("td", {"data-title":"PORT"}).text
        type=item.find("td", {"data-title":"类型"}).text
        host={type.lower() : type.lower()+"://"+ip+":"+str(port)}
        value = is_validity(host)
        print(value)
        if value == True:
            #sql="INSERT INTO ip_proxys(ip, status) VALUES('%s', %d);" %(type.lower()+"://"+ip+":"+str(port), 1)
            #od.insertdb(sql)
            print(host)

        else:
            pass
        m += 1
        if m>50:
            return 0
    n+=1
    time.sleep(2)
    if n==int(nav_num)+1:
        return 0
    kuaidlSoup(url, n, m)

#西刺代理解析
def xicidlSoup(url, n, m, db):
    html = getweb(url+str(n))
    soup = BeautifulSoup(html, 'html.parser')
    nav_num =soup.find_all('div', {'class':'pagination'})[0].find_all('a', )[-2].contents[0]

    trs = soup.find_all('tr')
    for i in range(1, len(trs)):
        tds = trs[i].find_all('td')
        ip = tds[1].contents[0]
        port = tds[2].contents[0]
        protocol = tds[5].contents[0].lower()
        value = is_validity(protocol, ip, port)

        if value == True:
            sql="INSERT INTO ip_proxys(protocol, ip, port, status) VALUES('%s', '%s', '%s', %d);" %(protocol, ip, port, 1)
            #mod.insertdb(sql)
            db.executedb(sql)
            m += 1
        else:
            pass
        if m>100:
            print("插入到数据库ip_proxys表中100条ip")
            return 0
    n+=1
    time.sleep(2)
    if n==int(nav_num)+1:
        print("遍历完所有页面，共插入到数据库ip_proxys表中 %d 条ip" %(m))
        return 0
    xicidlSoup(url, n, m, db)


def main():
    urls=['https://www.kuaidaili.com/free/inha/', 'http://www.xicidaili.com/nn/']
    #kuaidlSoup(urls[0],1,1)
    database=databases.Database('zhihu_info')
    database.connectdb()
    xicidlSoup(urls[1],1,1,database)
    database.closedb()
if __name__ == '__main__':
    main()