from django.shortcuts import render_to_response

from contact.models import UserInfo


__author__ = 'lilu'


def fetch_all_contact(request):
    stuffs = UserInfo.objects.all()
    stuffs_in_range = dict()
    for stuff in stuffs:
        if stuff.avatar != '':
            stuff.avatar = stuff.avatar + '64'
        first_letter = stuff.first_letter
        name_list = stuffs_in_range.get(first_letter)
        if name_list is None:
            name_list = []
            name_list.append(stuff)
        else:
            name_list.append(stuff)
        stuffs_in_range.update({first_letter: name_list})

    return render_to_response('contact_list.html', {'stuffs': stuffs_in_range})