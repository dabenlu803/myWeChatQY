import logging
from django.shortcuts import render_to_response
from wechatpy.enterprise import WeChatClient
from contact import wechat_config
from contact.models import UserInfo
import json

__author__ = 'lilu'


def show_contact_detail(request, param):
    # client = WeChatClient(wechat_config.CORP_ID, wechat_config.SECRET)
    # stuff = client.user.get(param)
    stuff = UserInfo.objects.get(user_id=param)
    attrs = []
    if stuff.extr_attr != '':
        attrs = eval(stuff.extr_attr).get('attrs', None)
    return render_to_response('contact_detail.html', {'item': stuff, 'attrs': attrs})