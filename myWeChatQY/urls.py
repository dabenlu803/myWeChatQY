"""myWeChatQY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from contact.contact_detail import show_contact_detail
from contact.views import requestHandler
from contact.contact_list import fetch_all_contact

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', requestHandler),
    url(r'^contact_all/$', fetch_all_contact),
    url(r'^contact_detail/$', show_contact_detail, name='contact_detail'),
]
