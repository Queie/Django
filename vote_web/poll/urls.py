from django.conf.urls import url, patterns
from poll import views   # from . import views    # '.'  : 현재폴더(앱이름)

urlpatterns = [
	url(r'^poll/$', views.index, name = 'index'),
	url(r'^poll/(?P<question_id>\d+)/$', views.detail, name='detail'),
	url(r'^poll/(?P<question_id>\d+)/vote/$', views.detail, name='detail'),
	url(r'^poll/(?P<question_id>\d+)/result/$', views.results, name='results'),
	url(r'^admin/', include(admin.site.urls)), # mysite 의 admin 을 재사용도 가능
]
