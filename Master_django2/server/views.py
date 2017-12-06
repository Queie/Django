from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime

# django 템플릿 활용함수
from django.template.loader import get_template, render_to_string
from django.template import Context

# django 템플릿 범용함수 (위의 2~3개의 함수들을 1개로 처리 )
from django.shortcuts import render
from django.core.mail import send_mail
from server.forms import ContactForm


# 간단한 text 출력
def hello(request):
	return HttpResponse("Hello Django Sites")


# request 객체의 '메소드' 내용을 출력
def requests(request):
	values = request.META.items()
	values = sorted(values)
	#values = values.sort()
	html = []
	for k, v in values:
		html.append('<tr> <td>{}</td> <td>{}</td> </tr>'.format(k, v))
	return HttpResponse('<< request dict info >> <table>%s</table>'%'\n'.join(html))


# 템플릿 내용을 직접 입력한 대로 출력
def current_datetime_01(request):
	now = datetime.datetime.now()      # TIME_ZONE = 'Asia/Seoul' 를 기준으로 현재시간을 설정
	now2 = datetime.datetime.utcnow()
	html = """<html><body>현재 시간은 <br></br>
			  {} <br></br>
			  {}</body></html>""".format(now, now2)
	return HttpResponse(html)


# 외부 Html 파일과 연결
# https://docs.djangoproject.com/en/1.11/topics/templates/#usage
def current_datetime_02(request):
	now = datetime.datetime.now()
	html = render_to_string('current_datetime.html', { 'current_date' : now })
	return HttpResponse(html)


# render() 함수로 단일화
# 위의 삽질은 뒤로하고 이것을 관용적으로 사용한다
def current_datetime(request):
	now = datetime.datetime.now()
	return render(request,                 # 인수1 : 요청
				 'current_datetime.html',  # 인수2 : 템플릿 (하위폴더 제한은 없다)
				  {'current_date':now} )   # 인수3 : context {dict 객체}


def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	# 시간 간격을 사용가능
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	html = """<html><body>In {} hour(s), It will be {}
			  </body></html>""".format(offset, dt)
	return HttpResponse(html)
from django.core.mail import send_mail


def contact(request):
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)

		# 1. 유효성 조건을 통과한 경우
		if form.is_valid():
			cd = form.cleaned_data
			try :
				# django form을 활용한 메일 보내기 (보안성 낮춤을 허용해야 한다)
				# https://docs.djangoproject.com/en/2.0/topics/email/
				# https://sendgrid.com/docs/Integrate/Frameworks/django.html
				send_mail(cd['subject'],cd['message'],
						  'muyongcctv@gmail.com',[cd['email']],fail_silently=False,)

				html = """ '{}' send to : <br></br>
				          <strong>{}</strong>""".format(cd['subject'], cd['email'])
				return HttpResponse(html)
				# return HttpResponseRedirect('/contact/thanks/')

			except Exception as e:
				# 정상적 웹연결 등이 안된경우
				html = """ '{}' 오류가 발생 """.format(e)
				return HttpResponse(html)

		# 2. forms.py의 유효성 검사를 통과 못한 경우
		else:
			errors.append('유효하지 않은 정보가 포함되어 있습니다 ')
			# form = ContactForm()
			return render(request, 'contact_form.html',{'form':form})

	# 3. POST 방식 오류가 발생한 경우 (새로 페이지를 갱신한다)
	form = ContactForm()
	return render(request, 'contact_form.html',{'form':form})