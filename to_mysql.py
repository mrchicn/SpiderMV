#@Time  : 2019/3/29 11:53
#@Author: www.mrchi.cn
#@File  : to_mysql.py
# -*- coding: UTF-8 -*-
import pymysql
# connect   地址  名字  密码  库
# 打开数据库连接
def Insert(jpg_url,describes):
    db =pymysql.connect("172.20.5.134","root","admin","Python_db", charset="utf8" )
    # 创建游标
    cursor=db.cursor()
    # 执行SQL  拼接真费事
    sql1  ="INSERT INTO dbmeinv(jpg_url,describes) VALUES ("
    sql2="\""+jpg_url+"\",\""+describes+"\");"
    sql3=sql1 + sql2
    # print(sql3)
    try:
        cursor.execute(sql3)
        db.commit()  # 没有提交数据库没有数据
        print("\t\tData Insert Success   .......")
    except:
       db.rollback()
    cursor.close()
    db.close()


