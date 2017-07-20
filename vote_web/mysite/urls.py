from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    # namespace 지정은  include() 함수 내부에 해야 한다!! <주의>
    url(r'^', include('elections.urls', namespace="elections")),
    url(r'^', include('kospi.urls', namespace="kospi")),
    url(r'^admin/', admin.site.urls),   # url( url주소, 실행 Python 함수)
]