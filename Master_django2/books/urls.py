#from django.conf.urls import url, include
from django.urls import include, re_path
from .views import search #, search_form

urlpatterns = [
    re_path(r'^$', search),   # request.GET : Get Query 대응을 위해 기본경로를 활용
    # url(r'^form/$', search_form),    # 단순 입력만 해서, if 명령으로 처리한다
]