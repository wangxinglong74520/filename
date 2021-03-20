#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : header.py
# @Time    : 2020/11/23 23:39
# @Author  : Merle
# @Site    : 
# ******************       *************
import random
from . import user_agents


def get_ua():
    # 随机的选择一个user-agent
    return random.choice(user_agents)
