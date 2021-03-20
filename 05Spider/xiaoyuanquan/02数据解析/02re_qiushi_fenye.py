#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 02re_qiushi_fenye.py
# @Time    : 2021/1/24 21:34
# @Author  : Merle
# @Site    : 
"""

"""
import time

"""
爬取糗事百科多页的数据
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
    # 创建一个保存文件夹
    filename = 'case/qiutuLibs'
    if not os.path.exists(filename):
        os.makedirs(filename)
    # 设置通用的url
    for i in range(1,14):
        url = f'https://www.qiushibaike.com/imgrank/page/{i}/'
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            page_text = resp.text
            ex = r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
            img_src_list = re.findall(ex, page_text, re.S)  # re.S d单行匹配  re.M 多行匹配
            # print(img_src_list)
            for src in img_src_list:
                # 拼接完整的图片url
                src = 'https:' + src
                # 请求图片的二进制数据信息
                img_data = requests.get(src, headers=headers).content
                # 生成图片名称
                img_name = src.split('/')[-1]
                imgPath = filename + '/' + img_name
                with open(imgPath, 'wb') as f:
                    f.write(img_data)
        time.sleep(0.2)
        print(f'正在爬取第{i}页图片')
    print('图片爬取完成!!!')