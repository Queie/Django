from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('elections.urls')),
    url(r'^', include('kospi.urls')),
    url(r'^admin/', admin.site.urls),   # url( url주소, 실행 Python 함수)
]