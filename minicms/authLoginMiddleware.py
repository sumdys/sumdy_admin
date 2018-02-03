#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-05 16:11:05
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
from django.conf import settings
from django.shortcuts import HttpResponseRedirect
import re

exclued_path = [re.compile(item) for item in settings.EXCLUDE_URL]

class authLoginMiddleware(object):
    def process_request(self, request):
        url_path = request.path
        for each in exclued_path:
            if re.match(each, url_path):
                return True
        if request.user.is_authenticated:
            return HttpResponseRedirect('/logout')
        else:
            return True

    def process_response(self, request, response):
        return response
