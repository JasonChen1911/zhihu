#coding=utf-8
import requests, json, MySQLdb
import methodOfDatabases as mod
import random
import databases

def getfollowering(urlToken, totals): 
    cookies={
        '_zap' : '605e4ac9-0877-4778-8137-8a1bac4b57da',
        'd_c0' : 'ABCsGugVQA2PTrKb4q51s2ZE6qF_9tXq4nc=|1520419009',
        '__DAYU_PP' : 'UyjQfivmb7Vu3mEUIjEQffffffff83d11a63a37f',
        'q_c1' : 'c2c54c071ba647e0ab91dca7b6b03926|1525338768000|1510837050000',
        'tgw_l7_route' : '4902c7c12bebebe28366186aba4ffcde',
        '_xsrf' : '157143bf-ac5e-4fce-8a46-b94b4254b1df',
        'capsion_ticket' : "2|1:0|10:1527846321|14:capsion_ticket|44:YjI2ZWUwNDQwYTNmNDg5Y2I1MmJlZTdhOGQzMjZjMTU=|e85549f8f81d5ec8d6bd3a7aa93849de05395a6679f88def1b3d250482aaecd4",
        'z_c0' : "2|1:0|10:1527846323|4:z_c0|92:Mi4xSkhwQUJRQUFBQUFBRUt3YTZCVkFEU1lBQUFCZ0FsVk5zMlAtV3dDZnB1OWw0cEh5UTJ3NFpZbVNHRElhN202RDNn|978dfe99c008ab9cb73d1518a69080abf46cbde22fb445446b5acafe1c103fef",
        '__utma' : '51854390.1963500968.1527846335.1527846335.1527846335.1',
        '__utmb' : '51854390.0.10.1527846335',
        '__utmc' : '51854390',
        '__utmz' : '51854390.1527846335.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        '__utmv' : '51854390.100--|2=registration_date=20170621=1^3=entry_date=20170621=1'
    }
    database = databases.Database('zhihu_info')
    database.connectdb()
    for x in xrange(0,totals/20):
        #offset=
        offset=20*x
        url='https://www.zhihu.com/api/v4/members/'+urlToken+'/followees?offset='+str(offset)+'&limit=20'
        print(url)
        Agents=['Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/60.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36']
        try:
            headers = {
                "Connection" : "keep-alive",
                "User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            }
            r=requests.get(url, headers=headers, cookies=cookies, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            obj_json = json.loads(r.text)
            print(obj_json)
            parsing_JSON(obj_json, database)
        except:
            print("111Error")
    database.closedb()

def parsing_JSON(json_dict, db):
    totals=json_dict['paging']['totals']
    followering_list=json_dict['data']
    for item in followering_list:
        sql="SELECT 1 FROM person_info_test WHERE url_token = '%s' limit 1;" %(item['url_token'])
        print("1", db.executedb(sql))
        if db.executedb(sql)==0:
            pass
        else:
            print("数据库中已存在")

def main():
    obj_json=getfollowering('guolaoxiong', 126)


if __name__ == '__main__':
    main()
