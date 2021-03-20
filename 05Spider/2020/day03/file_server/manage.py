#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : manage.py
# @Time    : 2020/12/14 21:41
# @Author  : Merle
# @Site    : 
"""

"""

from flask import request, jsonify
from __init__ import app
from werkzeug.datastructures import FileStorage


@app.route('/upload', methods=['POST'])
def upload():
    file1: FileStorage = request.files.get('file1')
    # file1.save()
    print(type(file1))
    print(file1.content_type, file1.filename)
    # 保存文件到static
    file1.save(f'static/{file1.filename}')
    return jsonify({'status', 'ok',})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
