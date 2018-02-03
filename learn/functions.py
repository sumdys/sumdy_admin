#!/usr/bin/env python
# -*- coding:utf-8 -*-
# timezone.now()
__author__ = 'sumdy'
import hashlib

def md5Function(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()