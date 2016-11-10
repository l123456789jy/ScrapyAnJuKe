# !/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


class AnJuKeDb:
    def __init__(self):
        pass

    # 返回数据库连接
    def getDbConnect(self):
        # 打开数据库连接
        db = MySQLdb.connect("localhost", "root", "root", "test")
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()
        print "Database version : %s " % data
        return db

    # 创建数据表ANJUKE的SQL语句,如果此表已经存在不在创建
    def createTable(self):
        try:
            sql = """CREATE TABLE IF NOT EXISTS  ANJUKE (
                 NAME  CHAR(255) ,
                 PHONE  CHAR(255),
                 ADDRESS CHAR(255))"""

            db = self.getDbConnect()
            db.cursor().execute(sql)
            db.close()
        except:
            print "except"

    # 插入数据
    def insertData(self):
        db = self.getDbConnect()
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = "INSERT  INTO ANJUKE(NAME,PHONE,ADDRESS)values(%s,%s,%s)"
        param = ("sss", 'Ass', 'MAsssN')
        cursor.execute(sql, param)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        cursor.close()


bdtb = AnJuKeDb()
bdtb.createTable()
bdtb.insertData()
