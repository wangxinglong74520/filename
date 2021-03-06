#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : es_.py
# @Time    : 2020/11/29 22:18
# @Author  : Merle
# @Site    : 
# ******************
"""
基于request库防装操作ElasticSearch搜索的函数(SDK)
"""
import requests
from urllib.parse import quote

INDEX_HOST = '119.3.170.97'
INDEX_PORT = 80


class ESIndex():
    """ES的索引库的类"""

    def __init__(self, index_name, doc_type):
        self.index_name = index_name
        self.doc_type = doc_type

    def create(self):
        # 创建索引库
        url = f'http://{INDEX_HOST}:{INDEX_PORT}/{self.index_name}'
        json_data = {
            "settings": {
                "number_od_shards": 5,
                "number_of_replicas": 1
            }
        }
        resp = requests.put(url, json=json_data)
        if resp.status_code == 200:
            print('创建所有成功')
            print(resp.json())

    def delete(self):
        # 删除索引库
        resp = requests.delete(f'http://{INDEX_HOST}:{INDEX_PORT}/{self.index_name}')
        if resp.status_code == 200:
            print('delete index ok')

    def add_doc(self, item: dict):
        # 向库中增加文档
        doc_id = item.pop('id', None)
        url = f'http://{INDEX_HOST}:{INDEX_PORT}/{self.index_name}/{self.doc_type}/'
        if doc_id:
            url += str(doc_id)
        resp = requests.post(url, json=item)
        if resp.status_code == 200:
            print(f'doc {url} 文档增加成功')

    def remove_doc(self, doc_id):
        # 删除文档
        url = f'http://{INDEX_HOST}:{INDEX_PORT}/{self.index_name}/{self.doc_type}/{doc_id}'
        resp = requests.delete(url)
        if resp.status_code == 200:
            print(f'delete {url} ok')

    def update_doc(self, item: dict):
        # 更新文档
        dict_id = item.pop('id')
        url = f'http://{INDEX_HOST}:{INDEX_PORT}/{self.index_name}/{self.doc_type}/{doc_id}'
        resp = requests.put(url, json=item)
        if resp.status_code == 200:
            print(f'{url} update ok ')
        pass

    def query(self, wd=None):
        # 查询
        q = quote(wd) if wd else ''
        url = f'http://{INDEX_HOST}:{INDEX_PORT}/{self.index_name}/_search?size=100'
        if q:
            url += f'&q={q}'
        resp = requests.get(url)
        datas = []
        if resp.status_code == 200:
            ret = resp.json()
            hits = ret['hits']['hits']

            if hits:
                for item in hits:
                    data = item['_source']
                    data['id'] = item['_id']
                    datas.append(data)
        return datas
if __name__ == '__main__':
    index = ESIndex('gushiwen','tuijian')
    index.create()
    index.add_doc({
        'id':1,
        'name':'disem',
        'price':19.5
    })
    index.add_doc({
        'id': 1,
        'name': 'disem',
        'price': 19.5
    })
    print(index.query())  # 打印所有的数据