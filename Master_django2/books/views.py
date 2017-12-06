from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from books.models import Book, Author


def search_form_(request):
	# 개별 App의 /templates 폴더를 우선 확인한다
	# 'templates/App이름 폴더/.html'로, /templates 와 혼동을 방지
	return render(request, 'books/search_form.html')  # 검색 form


def search_(request):
	if 'q' in request.GET: message = 'You searched for : {}'.format(request.GET['q'])
	else: message = 'You submitted an empty form.'
	return HttpResponse(message)


def search_(request):
	# 검색 form의 Get 전송으로, query url 이동시
	# request.GET['q'] 가 비있는지 함께 확인
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q)
		contain = {'books':books, 'query':q}
		# print('request : {} \n request.GET : {}'.format(
		# 	   request, request.GET))
		return render(request, 'books/search_result.html', contain)
	else:
		return render(request, 'books/search_form.html', {'error':True})



def search(request):
	errors = []
	# error = False

	if 'q' in request.GET:   # < 정상 <error = True> 조건 (비정상을 거러낸다) >
		q = request.GET['q']

		if not q:            # 1) q : 존재를 확인
			errors.append('내용을 입력해 주세요.')
			# error = True
		elif len(q) > 20:    # 2) q : 객체 길이 20을 넘는지 확인
			errors.append('글자가 20자를 넘습니다.')
			# error = True
		else:                # 1),2)를 통과한 < 정상객체 > q 를 처리
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'books/search_result.html',
				          {'books':books, 'query':q})
			print('errors',type(errors), errors)


	# < 위에서 탈락한 비정상 <error = True> 객체를 처리 >
	# .append() 안거친 경우, False와 동일
	print('errors',type(errors), errors)
	return render(request, 'books/search_form.html',{'errors':errors})
