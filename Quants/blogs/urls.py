from django.urls import path, re_path, include
from blogs.views import category, index, post, search

app_name = 'blogs'
urlpatterns = [
	re_path(r'^$',                     index, name='index'),
    re_path(r'^search/$',             search, name='search'),
	re_path(r'^(?P<pk>\d+)/$',          post, name='post'),
	re_path(r'^(?P<slug>[^\.]+)/$', category, name='category'),
]