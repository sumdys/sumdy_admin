#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sumdy'

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()