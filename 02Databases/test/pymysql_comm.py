#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time     :2020-12-14  19:28
# @Author   :Merle
# @File     :pymysql_comm.py
"""     """
import pymysql
from timeit import default_timer


def get_connection():
    """
    连接数据库
    :return: 返回连接
    """
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='admin123456',
        db='mysql')
    return conn


def check_it():
    conn = get_connection()

    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("select count(id) as total from Product")
    cursor.execute("show tables")
    # print(cursor.execute("show tables"))

    # # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    #
    # print("-- 当前数量: %d " % data['total'])

    # 关闭数据库连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    check_it()
