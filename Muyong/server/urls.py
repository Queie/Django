from django.contrib import admin
from django.urls import path, re_path, include

from server.views import HomeView   # 같은 폴더 파일연결
from profiles import views          # 별도  App 파일연결


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$',       HomeView.as_view(),  name='home'),
    re_path(r'^about/$', views.about, name='about'),
]

# from django.conf import settings
# from django.conf.urls.static import static

# if settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 	urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)