import logging
from django.shortcuts import render_to_response
from wechatpy.enterprise import WeChatClient
from contact import wechat_config

__author__ = 'lilu'


def show_contact_detail(request, param):
    logging.warn('param=%s', param)
    client = WeChatClient(wechat_config.CORP_ID, wechat_config.SECRET)
    stuff = client.user.get(param)
    logging.warn('user=%s', stuff)
    return render_to_response('contact_detail.html', {'item': stuff})