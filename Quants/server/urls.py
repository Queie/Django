from django.contrib import admin
from django.urls import path, re_path, include
from server.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

from .views import UserCreateView, UserCreateDone


urlpatterns = [

	# .as_view() : class 객체 연결시 메서드
	re_path(r'^$', HomeView.as_view(), name='home'),
	re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # Ckeditor 미리보기 URL
	# re_path(r'^martor/', include('martor.urls')),            # martor 미리보기 URL
	# re_path(r'^markdownx/', include('markdownx.urls')),      # markdown 미리보기 러프한 편집기

	# include()  : url을 '$' 닫지 않음
	re_path(r'^blog/',  include('blogs.urls', namespace="blog")),
	re_path(r'^stock/', include('stock.urls', namespace="stock")),
	re_path(r'^post/',  include('posts.urls', namespace="post")),
	re_path(r'^photo/', include('photo.urls', namespace="photo")),

    path('admin/', admin.site.urls),                           # admin Site 연결

    path('accounts/', include('django.contrib.auth.urls')),    # 기본인증(login) app 활성화
    path('accounts/register/',      UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDone.as_view(), name='register_done'),
    #re_path(r'^accounts/login/$', admin.site.urls),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# settings.py 의 'MEDIA_URL', 'MEDIA_ROOT'  패턴을 static()함수에 '추가적'연결