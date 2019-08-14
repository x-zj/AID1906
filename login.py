"""
练习:模拟登录注册行为
    * 创建用户表user 存储用户
    * 注册:将注册信息存储到数据库,用户名,不能重复
          基础信息包含用户名,密码
    * 登录:判断用户名密码是否正确
"""

import pymysql

class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             database='stu',
                             charset='utf8')

        # 创建游标对象 (操作数据库语句,获取查询结果)
        self.cur = self.db.cursor()

    # 注册
    def register(self,name,passwd):
        # 判断用户名
        sql = "select * from user where name='%s'"%name
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return False

        # 插入用户
        try:
            sql = "insert into user (name,passwd) values (%s,%s)"
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    # 登录
    def login(self,name,passwd):
        sql = "select * from user where name='%s' and passwd='%s'"%(name,passwd)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        if result:
            return True
        else:
            return False

    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

if __name__=="__main__":
    db = Database()
    while True:
        print("""
        ===============
        1. 注册  2. 登录
        ===============
        """)
        cmd = input("命令:")
        if cmd == '1':
            if db.register('张三','123'):
                print("注册成功")
                break
            else:
                print("注册失败")
        elif cmd == '2':
            if db.login('张三','123'):
                print("登陆成功")
                break
            else:
                print("登录失败")
        else:
            print("臣妾做不到啊!!!")










