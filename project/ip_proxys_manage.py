import requests
from bs4 import BeautifulSoup
import MySQLdb as mdb



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

def Soup(html):
    r_soup=BeautifulSoup(html, 'lxml')
    json_text = r_soup.body.contents[1].find_all("tbody")[0].find_all("tr")[0]#.find_all("td")
    for
    #obj_json = json.loads(json_text)
    print(json_text)


def main():
    url='https://www.kuaidaili.com/free/inha/3/'
    html=getweb(url)
    Soup(html)

if __name__ == '__main__':
    main()