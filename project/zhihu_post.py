#coding=utf-8
import requests
import json

def getfollowering(urlToken, totals): 
    cookies={
        '_zap' : '605e4ac9-0877-4778-8137-8a1bac4b57da',
        'z_c0' : "2|1:0|10:1512109831|4:z_c0|92:Mi4xSkhwQUJRQUFBQUFBQU1LMmEwVEVEQ1lBQUFCZ0FsVk5CMFVPV3dDMnFTRkh6Vm90V09YdEpYUVN5QXUtLXRtVU5B|3e3b5640a097a6d86ae26a7ef418bab26310e4ee15e0f2e3d0d1e4d2958626cf",
        'd_c0' : "ABCsGugVQA2PTrKb4q51s2ZE6qF_9tXq4nc=|1520419009",
        '__DAYU_PP' : 'UyjQfivmb7Vu3mEUIjEQffffffff83d11a63a37f',
        'q_c1' : 'c2c54c071ba647e0ab91dca7b6b03926|1525338768000|1510837050000',
        '__utmz' : '155987696.1525653518.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utma' : '155987696.394029749.1525653518.1526441527.1526976975.4',
        '_xsrf' : '1821e4bb-fbf8-4316-91d5-35914eea3f33',
        'tgw_l7_route' : 'b3dca7eade474617fe4df56e6c4934a3'
    }
    for x in xrange(0,totals/20):
        offset=20*x    
        url='https://www.zhihu.com/api/v4/members/'+urlToken+'/followees?offset='+str(offset)+'&limit=20'
        try:
            headers = {
                "Connection" : "keep-alive",
                "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
            }
            r=requests.get(url, headers=headers, cookies=cookies, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            obj_json = json.loads(r.text)
            parsing_JSON(obj_json)
        except:
            print("Error:status is ", r.raise_for_status)

def parsing_JSON(json_dict):
    totals=json_dict['paging']['totals']
    followering_list=json_dict['data']
    for item in followering_list:
        #print("名字 : %s" %(item['name'].encode('utf8')))
        #print("type : %s" %(item['type']))
        #print("url_token : %s" %(item['url_token']))


def main():
    obj_json=getfollowering('guolaoxiong', 309)


if __name__ == '__main__':
    main()
