#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time     :2021-02-19  10:47
# @Author   :Merle
# @File     :setting.py
"""     """
import pymysql


def connect_mysql(name):
    """
    :param name: 需要操作的数据库名称
    :return: 返回一个数据库连接对象 conn
    """
    conn = pymysql.connect(
        host='10.23.255.14',
        # host='localhost',
        user='root',
        passwd='tc123456',
        # passwd='admin123',
        db=name,
        port=3306
    )

    return conn


if __name__ == '__main__':
    conn = connect_mysql('test')
    cur = conn.cursor()
    cur.execute('select * from teacher')
    a = cur.fetchall()
    print([s for s in a])
