#from django.conf.urls import url, include
from django.urls import include, re_path, path
from django.contrib import admin

from server.views import requests, templates, current_datetime, hours_ahead, contact
from books import views

from server.views import HomeView



# https://docs.djangoproject.com/en/2.0/topics/http/urls/
urlpatterns = [
    re_path(r'^admin/',  admin.site.urls, name='admin'),
    re_path(r'^$',    HomeView.as_view(), name='home'     ),  # .as_view() : class를 연결
    re_path(r'^requests/$',     requests, name='request'  ),  # request 객체의 내용 확인
    re_path(r'^templates/$',   templates, name='templates'),  # 사용자 정의 filter
    re_path(r'^contact/$',       contact, name='contact'  ),  # 나에게 보대는 편지
    re_path(r'^time/$', current_datetime, name='time'     ),  # 현재시간
    re_path(r'^time/(\d{1,2})/$', hours_ahead),               # 추가시간
    # include()는 $로 닫지 않는다
    re_path(r'^books/', include('books.urls', namespace='books')),      # 도서제목BD 검색
    re_path(r'^games/', include('games.urls', namespace='games')),      # Restful API
]