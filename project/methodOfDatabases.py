#coding=utf-8
import MySQLdb as mdb

def connectdb():
    print("连接mysql....")
    try:
        db=mdb.connect("localhost", "root", "root147258", "zhihu_info", charset='utf8')
        print("mysql数据库已连接...")
        return db
    except:
        print("mysql数据库未连接...")

def insertdb(sql):
    db=connectdb()
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        db.commit();
        print("数据库操作成功...")
    except:
        db.rollback()
    db.close()

def verifydb(url_token, table):
    db=connectdb()
    cursor=db.cursor()
    sql="SELECT 1 FROM %s WHERE url_token = '%s' limit 1;" %(table, url_token)
    try:
        a = cursor.execute(sql)
    except:
        print("验证失败...") 
    db.close()
    return a

def main():
    print(verifydb('guolaoxiong1', 'person_info_test'))

if __name__ == '__main__':
    main()