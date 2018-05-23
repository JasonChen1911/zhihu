#coding=utf-8
import requests, json
from bs4 import BeautifulSoup


def getWeb(url):
    try:
		headers = {
            "Connection" : "keep-alive",
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        }
		r=requests.get(url, headers=headers, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
    except:
        print("Error:status is ", r.raise_for_status)

def Soup(html, userToken):
    r_soup=BeautifulSoup(html, 'html.parser')
    json_text = r_soup.body.contents[1].attrs['data-state']
    obj_json = json.loads(json_text)
    userInfo = obj_json['entities']['users'][userToken] 
    name=userInfo['name'] #名字
    gender=userInfo['gender'] #性别
    headline=userInfo['headline'] #一句话说明
    locations=userInfo['locations'][0]['name'] #地址
    major=userInfo['educations'][0]['major']['name'] #专业
    school=userInfo['educations'][0]['school']['name'] #学校
    job=userInfo['employments'][0]['job']['name'] #工作职位
    company=userInfo['employments'][0]['company']['name'] #公司名称
    description=userInfo['description'] #个人描述
    followingCount=userInfo['followingCount'] #关注了
    followerCount=userInfo['followerCount'] #关注着
    voteupCount=userInfo['voteupCount'] #获得赞同
    favoritedCount=userInfo['favoritedCount'] #获得收藏
    thankedCount=userInfo['thankedCount'] #获得感谢次数
    answerCount=userInfo['answerCount'] #回答次数
    articlesCount=userInfo['articlesCount'] #文章数量
    questionCount=userInfo['questionCount'] #提问次数
    followingTopicCount=userInfo['followingTopicCount'] #关注的话题
    followingQuestionCount=userInfo['followingQuestionCount'] #关注的问题


    print("学校 : %s" % (school.encode('utf8')))
    print("专业 : %s" % (major.encode('utf8')))
    print("关注了 : %s" % (followingCount))
    print("关注者 : %s" % (followerCount))
    print("获得赞同 : %s" % (voteupCount))
    print("获得收藏 : %s" % (favoritedCount))
    print("获得感谢 : %s" % (thankedCount))
    print("回答次数 : %s" % (answerCount))
    print("文章数量 : %s" % (articlesCount))
    print("提问次数 : %s" % (questionCount))
    print("关注的话题 : %s" % (followingTopicCount))
    print("关注的问题 : %s" % (followingQuestionCount))
    
def main():
    url = 'https://www.zhihu.com/people/guolaoxiong/activities'
    html=getWeb(url)
    Soup(html, 'guolaoxiong')

if __name__ == '__main__':
    main()
