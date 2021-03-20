#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 06_requests_yaopin.py
# @Time    : 2021/1/24 16:10
# @Author  : Merle
# @Site    : 
"""

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
    # 批量获取url
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data = {
        'on': 'true',
        'page': 2,
        'pageSize': 15,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': ''
    }
    resp = requests.post(url, data=data, headers=headers).json()
    id_list = []  # 存储企业id
    all_data_list = []  # 存储企业数据
    for dic in resp['list']:
        id_list.append(dic["ID"])
    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        deta_json = requests.post(url=post_url, data=data, headers=headers).json()
        # print(deta_json)
        all_data_list.append(deta_json)
    fp = open('case/yaopin.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
