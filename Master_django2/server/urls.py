#from django.conf.urls import url, include
from django.urls import include, re_path
from django.contrib import admin

from server.views import requests, current_datetime, hours_ahead, contact
from books import views


# https://docs.djangoproject.com/en/2.0/topics/http/urls/
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^requests/$', requests),
    re_path(r'^time/$', current_datetime),
    re_path(r'^time/(\d{1,2})/$', hours_ahead),  # 시간옵션을 활용

    # include()는 마지막 $로 닫지 않는다
    re_path(r'^search/', include('books.urls')),

    # 연락처 사용자 form
    re_path(r'^contact/$', contact),
]