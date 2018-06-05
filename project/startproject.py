#encoding=utf8
import databases
import IPProxys
import GetInformation
import zhihu_post


def Startproject(urlToken):
    followerCount, followingCount=GetInformation.ZhiHuSoup(urlToken)#followerCount 关注者, followingCount 关注了
    if followerCount >= 20 or followingCount >= 20:
        following_list=zhihu_post.getfollowering(urlToken, followingCount)
        for urlToken in followingCount:
            Startproject(urlToken)




def main():
    Startproject('guolaoxiong')

if __name__ == '__main__':
    main()
