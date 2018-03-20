from django.urls import path, re_path
from .views import PostDV, PostLV, PostTOL, Search, Create, Change, Update, Delete


app_name="post"
urlpatterns = [
	re_path(r'^$',                         PostLV.as_view(),  name='index'),
	re_path(r'^blog/(?P<slug>[-\w]+)/$',   PostDV.as_view(),  name='post_detail'),
	re_path(r'^tags/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tag_list'),
	re_path(r'^search/$',                  Search.as_view(),  name='search'),
	re_path(r'^add/$',                     Create.as_view(),  name='add'),
	re_path(r'^change/$',                  Change.as_view(),  name='change'),

	# post_change.html 에서 update/ delete 전달객체를 받는다
	re_path(r'^(?P<pk>[0-9]+)/update/$',   Update.as_view(),  name='update'),   # 99/upadte/
	re_path(r'^(?P<pk>[0-9]+)/delete/$',   Delete.as_view(),  name='delete'),   # 99/delete/
	# path('<int:pk>/update', Update.as_view(),  name='update'),
]

#	r'^(?P<slug>[-\w]+)/$  를 그대로 두니까,
#   post/search
#   post/tag  등의 인텍스를 PostDV의 일 부분으로 혼동하는 문제가 발생
#   DetailView 와 별개의 url 기능이 혼동 가능해서 이를 구분할 필요가 있음


# re_path(r'^update/(?P<pk>[0-9]+)/$',   Update.as_view(),  name='update'),   # 99/upadte/
