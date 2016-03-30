import logging

from django.shortcuts import render_to_response
from wechatpy.enterprise import WeChatClient

from contact import wechat_config


__author__ = 'lilu'


def fetch_all_contact(request):
    client = WeChatClient(wechat_config.CORP_ID, wechat_config.SECRET)
    access_token = client.fetch_access_token()
    departments = client.department.get()
    stuffs = []
    for department in departments:
        department_id = department.get('id')
        stuffs.extend(client.user.list(department_id))
    stuffs_in_range = dict()
    for stuff in stuffs:
        # stuff['avatar'] = stuff['avatar'] + '64'
        first_letter = get_cn_first_letter(stuff['name'], type(stuff['name']).__name__)
        name_list = stuffs_in_range.get(first_letter)
        if name_list is None:
            name_list = []
            name_list.append(stuff)
        else:
            name_list.append(stuff)
        stuffs_in_range.update({first_letter: name_list})
    # for k, v in stuffs_in_range.items():
    # logging.warn('key=%s,value=%s', k, v)

    return render_to_response('contact_list.html', {'stuffs': stuffs_in_range})


def get_cn_first_letter(str, codec='UTF8'):
    # logging.warn('str before=%s', str)
    if codec != "GBK":
        if codec != 'unicode':
            str = str.decode(codec)
        str = str.encode('GBK')
    # logging.warn('str after=%s', str)
    if str < "\xb0\xa1" or str > "\xd7\xf9":
        return ""
    if str < "\xb0\xc4":
        return "A"
    if str < "\xb2\xc0":
        return "B"
    if str < "\xb4\xed":
        return "C"
    if str < "\xb6\xe9":
        return "D"
    if str < "\xb7\xa1":
        return "E"
    if str < "\xb8\xc0":
        return "F"
    if str < "\xb9\xfd":
        return "G"
    if str < "\xbb\xf6":
        return "H"
    if str < "\xbf\xa5":
        return "J"
    if str < "\xc0\xab":
        return "K"
    if str < "\xc2\xe7":
        return "L"
    if str < "\xc4\xc2":
        return "M"
    if str < "\xc5\xb5":
        return "N"
    if str < "\xc5\xbd":
        return "O"
    if str < "\xc6\xd9":
        return "P"
    if str < "\xc8\xba":
        return "Q"
    if str < "\xc8\xf5":
        return "R"
    if str < "\xcb\xf9":
        return "S"
    if str < "\xcd\xd9":
        return "T"
    if str < "\xce\xf3":
        return "W"
    if str < "\xd1\x88":
        return "X"
    if str < "\xd4\xd0":
        return "Y"
    if str < "\xd7\xf9":
        return "Z"
