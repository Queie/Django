from django.urls import re_path
from .views import AlbumDV, AlbumLV, PhotoDV


app_name="photo"

urlpatterns = [
	re_path(r'^$',                   AlbumLV.as_view(), name='index'),
	re_path(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),
	re_path(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
]
# /
# /album/999
# /photo/999