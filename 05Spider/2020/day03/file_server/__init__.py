#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2020/12/14 21:41
# @Author  : Merle
# @Site    : 
"""

"""

from flask import Flask

app = Flask(__name__,
            static_url_path='/s',
            static_folder='static')