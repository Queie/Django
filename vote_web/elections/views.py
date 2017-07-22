from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
# Create your views here.
from elections.models import Candidate , Poll, Choice # models.py 객체를 활용한다
from django.db.models import Sum

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy # reverse()보다 안정적 로딩

import datetime



# string 을 Html 로 바로 출력한다.
def index_old(request):
	candidates = Candidate.objects.all()
	str = ''  # html 초기화
	for candidate in candidates:
		str +='<p> {} 기호 {}번 ({})<br>'.format(\
				candidate.name, candidate.party_number, candidate.area)
		str += candidate.introduction+'<p>'
	return HttpResponse(str) # 위 str 텍스트를 웹 화면에 출력



# render() 파이썬 객체를 html 전달
# manage.py -->  urls.py --> views.py <--> models.py
                             # L..Templates   (Model, View(html) , Controlers(views.py))
def index(request):
	candidates = Candidate.objects.all()
	context = {'candidates':candidates}                      # Html 전달할 객체를 특정
	return render(request, 'elections/index.html', context)



# area 객체에 따라서 다르게 반응한다.
def areas_old(request, area):
	return HttpResponse(area)



def areas(request, area):
	today = datetime.datetime.now()
	try:
		# .get() : 해당 조건의 index를 모두 저장  # Many to Many
		# ex) poll.area , poll.start_date 하면 개별 내용을 호출가능 !!
		poll = Poll.objects.get(area = area,\
				start_date__lte=today, end_date__gte=today)

		# .filter() : 컬럼('area')의 해당 인덱스 데이터만 호출 (객체 1개)
		candidates = Candidate.objects.filter(area = area)

	except:
		poll = None
		candidates = None
	context = {'candidates':candidates, 'area':area, 'poll':poll }
	return render(request, 'elections/area.html',context)



# html 에서 Post 로 객체를 전달받아서 새로운 연산을 처리한다.
def polls(request, poll_id):

	poll = Poll.objects.get(pk=poll_id)
	selection = request.POST['choice']

	try:
		# {{poll.id}} {{candidate.id}} 를 post 로 받으면,
		# django back-hand는 'poll_id' , 'candidate_id'로 받는다.
		# models.py의 객체와 다른 문법적용
		choice = Choice.objects.get(poll_id = poll_id, candidate_id = selection)
		choice.votes += 1
		choice.save()

	except:
		# 투표 초기값이 없을 때
		choice = Choice(poll_id = poll_id, candidate_id = selection, votes = 1 )
		choice.save()

	# HttpResponseRedirect() 함수 처리결과를
	# urls.py (/areas/{}/results/$ --> result() : 종속함수) 로 다른함수에 전달
	#return HttpResponseRedirect("/areas/{}/results".format(poll.area))

	# namespace 문법을 일동일하게 함수에도 활용 (이게 더 적합하다!!)
	# args = ( ,) 꼭 tuple 로 지정!!!!
	# (안그러면 낱말 단위로 쪼개더라... )
	return HttpResponseRedirect(reverse('elections:results', args=(poll.area,)))



# 투표결과를 확률로 연산하는 모듈
def results(request, area):
	# 조건에 맞는 index 데이터를 호출
	candidates = Candidate.objects.filter(area = area)
	polls = Poll.objects.filter(area = area)
	poll_results = []

	for poll in polls:

		# 연산결과를 {dict}에 저장
		result = {}
		result['start_date'] = poll.start_date
		result['end_date'] = poll.end_date

		# 확률의 분모값
		# filter(조건문)와 일치하는 객체들의 합
		total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))

		# print("################", total_votes)
		# terminal에서 total_votes 객체가 어떻게 출력되는지 확인
		# terminal...  ################ {'votes__sum': 4}
		result['total_votes'] = total_votes['votes__sum']

		rates = []
		for candidate in candidates:
			try:
				choice = Choice.objects.get(poll_id = poll.id, candidate_id = candidate.id)
				# round(객체 , 1) : 소숫점 1자리 까지만 출력
				rates.append(
					round(choice.votes * 100 / result['total_votes'], 1)) # 백분율 계산
			except:
				rates.append(0)
		result['rates'] = rates
		print(len(result))
		poll_results.append(result)

	# 위에서 내부처리 결과를 새로운 html에 연결해서 출력
	context = {'candidates':candidates, 'area':area, 'poll_results':poll_results}
	return render(request, 'elections/result.html', context)



# 404 오류의 처리
def candidates(request,name):

	# candidate =Candidate.objects.get(name = name) 의 예외적 404를 1줄로 처리
	candidate = get_object_or_404(Candidate, name = name)

	# try:
	# 	candidate =Candidate.objects.get(name = name)

	# except:
	# 	# 함수별 404 오류를 처리
	# 	# return HttpResponseNotFound(" 없는 페이지 입니다.")

	# 	# 일괄적 404 오류로 처리
	# 	raise Http404

	return HttpResponse(candidate)