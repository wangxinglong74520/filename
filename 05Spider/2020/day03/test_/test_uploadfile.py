#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : test_uploadfile.py
# @Time    : 2020/12/14 21:53
# @Author  : Merle
# @Site    : 
"""

"""
import requests

resp = requests.post('http://0.0.0.0:8000/upload/', files={
    'file1': ('code.png', open('code.png', 'rb'))
})
print(resp.json())
