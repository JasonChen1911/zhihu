# encoding=utf8
import MySQLdb as mdb

class Database:

    def __init__(self, database):
        self.database = database
        self.table = table
        self.__username = 'root'
        self.__password = 'root147258'
        self.__db = None

    def connectdb(self):
        print("连接数据库...")
        try:
            self.__db = mdb.connect("localhost", self.__username, self.__password, self.database, charset='utf8')
            print("数据库已连接...")

        except:
            print("数据库连接失败...")

    def executedb(self, sql):
        if self.__db:
            cursor = self.__db.cursor()
            try:
                a = cursor.execute(sql)
                db.commit()
                print("数据库操作成功")
            except:
                db.rollback()
            return a
        else:
            print("数据库未连接, 请先连接数据库...")

    def closedb(self):
        if self.__db:
            self.__db.close()
            print("数据库连接已断开...")
        else:
            print("数据库未连接, 请先连接数据库...")