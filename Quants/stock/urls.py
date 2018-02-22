from django.urls import path, re_path, include
from stock.views import index, codes


app_name = 'stock'
urlpatterns = [
	re_path(r'^$',                   index, name='index'),
	re_path(r'^(?P<slug>[^\.]+)/$',  codes, name='codes'),
	#re_path(r'^new/$',               new38, name='new'),
    # re_path(r'^search/$',         search, name='search'),
]