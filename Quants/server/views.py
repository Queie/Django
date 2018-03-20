#from django.views.generic.base import TemplateView  # 2.0 에서도 되지만 아래로 통합됨
from django.views.generic import TemplateView


# Main Template
class HomeView(TemplateView):
	template_name = 'home.html'


# reverse() 로 url 이동시, time 지체 발생시 사용
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


# User login Page 를 별도로 관리한다
# 별도 설장하지 않으면 Login 후 admin 페이지로 바로 이동
class UserCreateView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')   # url name 으로 완료 후 이동

# 완성결과 출력
class UserCreateDone(TemplateView):
	template_name = 'registration/register_done.html'