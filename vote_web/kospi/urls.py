from django.conf.urls import url

# from . import views    # '.'  : 현재 작업폴더(앱이름)
# 위 문법보단 이게 확실하다.
from kospi import views


# HTML 에서 namespace로 연결 ( layout.html )
# app_name = 'kospi'


urlpatterns = [
    url(r'^kospi/$', views.index, name = 'chart'),
    # '.' : 모든객체 가능 (/도 포함해서 1개 객체로 인식한다)
]