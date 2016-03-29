from django.shortcuts import render_to_response

__author__ = 'lilu'

def show_contact_detail(request):
    return render_to_response('contact_detail.html')