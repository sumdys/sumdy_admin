#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'
from base64 import b64decode
import time
import os

#上传图片
def uploadFiles(img,dir=''):
    file_name = ''
    try:
        # 保存路经
        file_path = os.path.join('upload/images/'+dir)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        imageData = img.split('base64,', 1)
        image_data = b64decode(imageData[1])
        image_name = str(int(time.time())) + ".jpg"
        file_name = file_path+image_name
        # fp = open(file_path, 'wb')
        # fp.write(image_data)
        # fp.close()
        # 上传文件保存
        with open(file_name, 'wb') as f:
            f.write(image_data)
            f.close()
    except Exception as e:
        print(e)
    return file_name

