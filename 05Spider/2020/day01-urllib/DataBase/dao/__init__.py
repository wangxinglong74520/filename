#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2020/11/22 16:42
# @Author  : Merle
# @Site    : 
# ******************       *************
import pymysql
from pymysql.cursors import DictCursor


class Connection():
    def __init__(self):
        self.conn = pymysql.Connect(
            host="localhost",
            user="root",
            passwd="admin123",
            port=3306,
            db="stu",
        )

    def __enter__(self):
        # DictCursor针对查询结果进行dict化
        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # 回滚事物
            self.conn.rollback()
            # 日志收集异常信息,上报给服务器
        else:
            # 提交事物
            self.conn.commit()

    def close(self):
        try:
            self.conn.close()
        except:
            pass
