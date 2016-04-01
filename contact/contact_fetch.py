import logging
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from wechatpy.enterprise import WeChatClient
from contact import wechat_config
from contact.models import DepartmentInfo
from contact.models import UserInfo
from django.http import HttpResponse
from xpinyin import Pinyin
from operator import attrgetter
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'lilu'


def contact_fetch(request, param='0'):
    logging.warn('param = %s', param)
    if param != '0':
        client = WeChatClient(wechat_config.CORP_ID, wechat_config.SECRET)
        departments = client.department.get()
        DepartmentInfo.objects.all().delete()
        UserInfo.objects.all().delete()
        user_info_list = []
        for department in departments:
            department_info = DepartmentInfo()
            department_info.department_id = department.get('id', None)
            department_info.department_name = department.get('name', '')
            department_info.order = department.get('order', None)
            department_info.parent_id = department.get('parentid', None)
            department_info.save()
            users = client.user.list(department['id'])
            for user in users:
                user_info = UserInfo()
                user_info.user_id = user.get('userid', None)
                user_info.user_name = user.get('name', '')
                user_info.gender = user.get('gender', 0)
                user_info.department_id = user.get('department', '')
                user_info.position = user.get('position', '')
                user_info.mobile = user.get('mobile', '')
                user_info.avatar = user.get('avatar', '')
                user_info.email = user.get('email', '')
                user_info.weixin_id = user.get('weixinid', '')
                user_info.status = user.get('status', '')
                user_info.extr_attr = user.get('extattr', '')
                user_info_list.append(user_info)
        sorted_list = sorted_by_first_letter(user_info_list)
        save_user_info_in_db(sorted_list)
        return HttpResponseRedirect('/contact_fetch_success/')
    return render_to_response('contact_fetch.html')


def contact_fetch_success(request):
    return HttpResponse('Success')


def sorted_by_first_letter(user_list):
    p = Pinyin()
    for user in user_list:
        user.pinyin = p.get_pinyin(user.user_name, u'')
        if user.pinyin != '':
            user.first_letter = user.pinyin.upper()[0]
        else:
            user.first_letter = ''
    return sorted(user_list, key=attrgetter('pinyin'), reverse=False)


def save_user_info_in_db(user_list):
    for user in user_list:
        user.save()
