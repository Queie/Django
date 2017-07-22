from django.conf.urls import url, include
from django.contrib import admin

from mysite import views # 메인페이지 만들기

urlpatterns = [

    # 'as_view()' 는 Class 객체를 호출시 사용
    # url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', views.HomeView, name='home'),

    # namespace 지정은  include() 함수 내부에 해야 한다!! <주의>
    url(r'^elections/', include('elections.urls', namespace="elections")),
    url(r'^kospi', include('kospi.urls', namespace="kospi")),
    url(r'^admin/', admin.site.urls),   # url( url주소, 실행 Python 함수)
]

# ^ : Start , $: End  , [] : List , | : Filter
# . : All   , * : {0,}, +  : {1,}
# \d  : [0-9]
# \w  : [0-9a-zA-Z_]
# {n} : n번 반복      , {m:n} : Max m Min n