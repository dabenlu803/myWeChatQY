import logging
import locale
from django.shortcuts import render_to_response
from wechatpy.enterprise import WeChatClient
from contact import wechat_config

__author__ = 'lilu'


def fetch_all_contact(request):
    client = WeChatClient(wechat_config.CORP_ID, wechat_config.SECRET)
    access_token = client.fetch_access_token()
    departments = client.department.get()
    stuff = []
    for department in departments:
        department_id = department.get('id')
        stuff.extend(client.user.list(department_id))
    logging.warn('size=%d,stuff=%s', stuff.__len__(), stuff)
    # response = HttpResponse('' + access_token.get('access_token', None), content_type="text/plain")
    # return response
    return render_to_response('contact_list.html', {'stuffs': stuff})
