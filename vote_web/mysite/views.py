# Home View 를 새로 만들어야 한다.
from django.shortcuts import render , get_object_or_404
from django.views.generic.base import TemplateView
from django.http import HttpResponse
import datetime


def HomeView(request):
	now = datetime.datetime.now()
	context = {'date' : now}
	return render(request, 'home.html', context)


# urls.py 에선  .as_view() 가 필요
class HomeView_1(TemplateView):
	template_name = 'home.html'


# Html 를 직접 입력 한 경우
def HomeView_html(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now {0} </body></html>".format(now)
	return HttpResponse(html)

