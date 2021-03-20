#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @time     :2021-02-19  15:18
# @Author   :Merle
# @File     :inserts_database.py
"""     """
from test.setting import connect_mysql
from faker import Faker
import random


def insert_data(lists):
    """
    :param lists:
    :return: 插入test数据库函数
    """
    conn = connect_mysql('test')
    cur = conn.cursor()
    sql = 'insert into user(`name`,`password`,`age`,`tel`) values(%s,%s,%s,%s)'
    cur.executemany(sql, lists)
    conn.commit()
    cur.close()
    conn.close()


def get_data():
    ls = []
    fake = Faker(locale='zh_CN')
    for i in range(1000):
        name = fake.name()
        phone = fake.phone_number()
        age = random.randint(1, 100)
        password = fake.password(special_chars=False)
        ls.append((name, password, age, phone))
        # print(password)
    print(ls)
    insert_data(ls)
    print('数据插入成功')


get_data()
