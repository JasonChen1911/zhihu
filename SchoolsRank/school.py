# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import bs4
import csv

def getHtml(url):
    #构建 Request Header
    Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    headers = {
        'User-Agent' : Agent
    }
    try:
        r = requests.get(url, headers = headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("请求失败！")
def parseHtml(html):
    school_lists = []
    school_lists.append(['排名', '学校名称', '省市', '总分', '生源质量（新生高考成绩得分）', '培养结果（毕业生就业率）', '社会声誉（社会捐赠收入·千元）', '科研规模（论文数量·篇）', '科研质量（论文质量·FWCI）', '顶尖成果（高被引论文·篇）', '顶尖人才（高被引学者·人）', '科技服务（企业科研经费·千元）', '成果转化（技术转让收入·千元）', '学生国际化（留学生比例）'])
    r_soup = BeautifulSoup(html, "html.parser")
    for tr in r_soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            school_info = []
            for item in tds:
                value = item.string
                if value != None:
                    school_info.append(value.encode('utf8'))
                else:
                    school_info.append(value)
            school_lists.append(school_info)
    return school_lists

def writeCSV(datas):
    csvfile = file('./schoolranking.csv', 'w')
    writer = csv.writer(csvfile)
    writer.writerows(datas)
    csvfile.close()


def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = getHtml(url)
    school_lists = parseHtml(html)
    writeCSV(school_lists)




if __name__ == '__main__':
    main()
