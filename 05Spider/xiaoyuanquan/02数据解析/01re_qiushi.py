#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 01re_qiushi.py
# @Time    : 2021/1/24 20:59
# @Author  : Merle
# @Site    : 
"""
爬取糗事百科的数据
"""
import re
import requests
from utils.header import get_ua
import os
import json

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': get_ua()
}

if __name__ == '__main__':
    #
    url = 'https://www.qiushibaike.com/imgrank/'
    # 创建一个保存文件夹
    filename = 'case/qiutuLibs'
    if not os.path.exists(filename):
        os.makedirs(filename)
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        page_text = resp.text
        ex = r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)  # re.S d单行匹配  re.M 多行匹配
        print(img_src_list)
        for src in img_src_list:
            # 拼接完整的图片url
            src = 'https:' + src
            # 请求图片的二进制数据信息
            img_data = requests.get(src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            imgPath = filename + '/' + img_name
            print(imgPath)
            with open(imgPath, 'wb') as f:
                f.write(img_data)
        print('图片保存成功!!!')
