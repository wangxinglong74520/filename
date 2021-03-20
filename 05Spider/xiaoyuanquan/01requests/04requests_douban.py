#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 04requests_douban.py
# @Time    : 2021/1/24 15:38
# @Author  : Merle
# @Site    : 
"""
    获取豆瓣排行榜
"""
import requests
from utils.header import get_ua
import json
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': get_ua()
}
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    data ={
        'type': 5,
        'interval_id': '100:90',
        'action': '',
        'start': 0,  # 从库中的第几部电影
        'limit': 60  # 一次取出的个数
    }
    response = requests.get(url,headers=headers,params=data)
    print(response.text)
    list_data = response.json()
    print(len(list_data))
    print(list_data)

    # for i in range(len(list_data)):
    #     mover_name = list_data[i]['title']
    #     mover_url = list_data[i]['url']
    #     print(mover_name,mover_url)
    #
    # fp = open('case/douban.json','w',encoding='utf-8')
    # json.dump(list_data,fp=fp,ensure_ascii=False)
    # print('over')




