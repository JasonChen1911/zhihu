#coding=utf-8
import requests, json, MySQLdb
from bs4 import BeautifulSoup
import methodOfDatabases as mod

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

def connectdb():
    keys=(url_token, gender, name, headline, location, school, major, company, job, followingCount, followerCount, voteupCount,favoritedCount, thankedCount, answerCount, articlesCount, questionCount, followingTopicCount, followingQuestionCount)
    db=MySQLdb.connect("localhost", "root", "root147258", "zhihu_info", charset='utf8')
    cursor=db.cursor()
    sql= "INSERT INTO person_info_test(url_token, gender, name, headline, location, school, major, company, job, followingCount, followerCount, voteupCount,favoritedCount, thankedCount, answerCount, articlesCount, questionCount, followingTopicCount, followingQuestionCount) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d);" %(url_token, gender, name, headline, location, school, major, company, job, followingCount, followerCount, voteupCount,favoritedCount, thankedCount, answerCount, articlesCount, questionCount, followingTopicCount, followingQuestionCount)
    
    try:
        a=cursor.execute(sql)
        print(a)
        db.commit()
    except:
        db.rollback()
        print("fail")
    
    db.close()

def Soup(html, userToken):
    r_soup=BeautifulSoup(html, 'html.parser')
    json_text = r_soup.body.contents[1].attrs['data-state']
    obj_json = json.loads(json_text)
    userInfo = obj_json['entities']['users'][userToken] 
    user_info={}
    user_info['name']=userInfo['name'] #名字
    user_info['url_token']=userInfo['urlToken']
    #性别
    try:
        if userInfo['gender'] == 1: 
            user_info['gender'] = 'M'
        elif userInfo['gender'] == 2:
            user_info['gender'] = 'F'
        else:
            user_info['gender'] = 'N'
    except:
        user_info['gender']='N'
    try:
        user_info['headline']=userInfo['headline'] #一句话说明
    except:
        user_info['headline']=''
    try:
        user_info['location']=userInfo['locations'][0]['name'] #地址
    except:
        user_info['location']=''
    try:
        user_info['major']=userInfo['educations'][0]['major']['name'] #专业
    except:
        user_info['major']=''
    try:
        user_info['school']=userInfo['educations'][0]['school']['name'] #学校
    except:
        user_info['school']=''
    try:
        user_info['job']=userInfo['employments'][0]['job']['name'] #工作职位
    except:
        user_info['job']=''
    try:
        user_info['company']=userInfo['employments'][0]['company']['name'] #公司名称
    except:
        user_info['company']=''
    user_info['followingCount']=userInfo['followingCount'] #关注了
    user_info['followerCount']=userInfo['followerCount'] #关注着
    user_info['voteupCount']=userInfo['voteupCount'] #获得赞同
    user_info['favoritedCount']=userInfo['favoritedCount'] #获得收藏
    user_info['thankedCount']=userInfo['thankedCount'] #获得感谢次数
    user_info['answerCount']=userInfo['answerCount'] #回答次数
    user_info['articlesCount']=userInfo['articlesCount'] #文章数量
    user_info['questionCount']=userInfo['questionCount'] #提问次数
    user_info['followingTopicCount']=userInfo['followingTopicCount'] #关注的话题
    user_info['followingQuestionCount']=userInfo['followingQuestionCount'] #关注的问题

    #connectdb(url_token, gender, name, headline, location, school, major, company, job, followingCount, followerCount, voteupCount,favoritedCount, thankedCount, answerCount, articlesCount, questionCount, followingTopicCount, followingQuestionCount)
    return user_info

def main():
    url_token='xiao-chou-xian-sheng-21-79'
    url = 'https://www.zhihu.com/people/'+url_token+'/activities'
    html=getWeb(url)
    Soup(html, url_token)
    mod.verifydb(url_token, 'person_info_test')

if __name__ == '__main__':
    main()
