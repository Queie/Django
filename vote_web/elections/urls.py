from django.conf.urls import url

# from . import views    # '.'  : 현재 작업폴더(앱이름)
# 위 문법보단 이게 확실하다.
from elections import views


# HTML 에서 namespace로 연결 ( layout.html )
# app_name = 'elections'


urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    # '.' : 모든객체 가능 (/도 포함해서 1개 객체로 인식한다)

    # <area> 객체를 views.areas 에 전달
    # <area>[가-힣] : <area> 는 한글객체만 가능
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas, name='areas') ,
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results, name = 'results') ,

    # <poll_id> 는 '\d+' 숫자만 가능
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),

    # <name> 은 '한글'객체만 가능
    url(r'^candidates/(?P<name>[가-힣]+)/$',views.candidates),
]