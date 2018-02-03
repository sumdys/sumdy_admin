#!/usr/bin/env python
# -*- coding:utf-8 -*-
# timezone.now()
__author__ = 'sumdy'

from django.conf import settings

def global_setting(request):
    return {'STATIC_ROOT':settings.STATIC_ROOT,'SITE_NAME':settings.SITE_NAME,'STATIC_URL':settings.STATIC_URL,'STATIC_PATH':settings.STATIC_PATH}