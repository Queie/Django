from django.urls import include, re_path, path
from games.views import game_list, game_detail

# include() 연결시 App을 선언 (중복, 오류를 방지)
app_name = 'games'
urlpatterns = [
    re_path(r'^$',                    game_list, name='list'  ),
    re_path(r'^(?P<pk>[0-9]+)/$',  game_detail, name='detail'),
]