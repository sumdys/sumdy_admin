#!/usr/bin/env python
# -*- coding:utf-8 -*-
# timezone.now()
__author__ = 'sumdy'

from django import forms

class AddForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    real_name = forms.CharField()
    password = forms.CharField()
    addr = forms.CharField()
    email = forms.EmailField()
    head_url = forms.FileField()
