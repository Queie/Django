from django.contrib import admin
from django.urls import path, re_path, include
from server.views import HomeView


urlpatterns = [
	# .as_view() : class 객체 연결시 메서드
	re_path(r'^$', HomeView.as_view(), name='home'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # Ckeditor 미리보기 URL
	# re_path(r'^martor/', include('martor.urls')),            # martor 미리보기 URL
	# re_path(r'^markdownx/', include('markdownx.urls')),      # markdown 미리보기 러프한 편집기

	# include()  : url을 '$' 닫지 않음
	re_path(r'^blogs/', include('blogs.urls', namespace="blogs")),
	re_path(r'^stock/', include('stock.urls', namespace="stock")),
    path('admin/', admin.site.urls),
]