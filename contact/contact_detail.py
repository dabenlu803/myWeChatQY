from django.shortcuts import render_to_response

from contact.models import UserInfo


__author__ = 'lilu'


def show_contact_detail(request, param):
    stuff = UserInfo.objects.get(user_id=param)
    attrs = []
    if stuff.extr_attr != '':
        attrs = eval(stuff.extr_attr).get('attrs', None)
    return render_to_response('contact_detail.html', {'item': stuff, 'attrs': attrs})