from django.http import HttpResponse
from wechatpy.enterprise import WeChatClient

__author__ = 'lilu'

from contact import wechat_config
import logging


def fetch_all_contact():
    client = WeChatClient(wechat_config.CORP_ID, wechat_config.SECRET)
    access_token = client.fetch_access_token()
    department = client.department.get()
    logging.warn('department=%s', department)
    response = HttpResponse('' + access_token.get('access_token', None), content_type="text/plain")
    return response
