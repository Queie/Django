from django.views.generic.base import TemplateView


# Main Template를 설정
class HomeView(TemplateView):
	template_name = 'home.html'
