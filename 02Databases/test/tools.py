#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time     :2020-12-11  11:44
# @Author   :Merle
# @File     :tools.py
"""     """
import pymysql


def get_mysql():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='admin123',
        db='test',
        port=3306
    )
    cur = conn.cursor()
    aa = cur.execute('select * from user')
    # 创建数据表
    # cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
    # sqli = "insert into student values(%s,%s,%s,%s)"
    # cur.executemany(sqli, [
    #     ('3', 'Tom', '1 year 1 class', '6'),
    #     ('3', 'Jack', '2 year 1 class', '7'),
    #     ('3', 'Yaheng', '2 year 2 class', '7'),])
    # 打印表中的多少数据
    # info = cur.fetchmany(aa)
    # print(info)
    # for ii in info:
    #     print(ii)
    # # 获取第一行数据
    # row_1 = cur.fetchone()
    # print(row_1)
    # # 获取前n行数据
    # row_2 = cur.fetchmany(3)
    # print(row_2)
    # 获取所有数据
    row_3 = cur.fetchall()
    print(row_3)
    cur.close()
    conn.close()


if __name__ == '__main__':
    get_mysql()
