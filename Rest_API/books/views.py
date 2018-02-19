from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from books.models import Book, Author

# django 사용자 필터
from django import template
register = template.Library()


def filters(request):
	@register.filter()
	def books_for_author(author):
		books = Book.objects.filter(authors__id = author.id)
		return {'books':books}
	return render(request, 'books/filters.html')

# book_list 기본 페이지 설정
def book_list(request):
	return render(request, 'books/list.html')

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



# Image 출력
def my_image(request):
	image_data = open('/books/data/image.png','rb').read()
	return HttpResponse(image_data, content_type="image/png")


# CSV 생성 및 출력
import csv
def csv_fils(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename = "somefile.csv"'

	writer = csv.writer(response)
	writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
	writer.writerow(['Second row', 'A', 'B', 'C', 'Testing'])
	return response


from django.template import loader, Context

def csv_files_2(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somecsv.csv"'

	csv_data = (
		('first row', 'A', 'B', 'C', 'D'),
		('second row', '102','202','302','402'),
		)
	t = loader.get_template('books/csv_table.html')
	c = Context( {'data':csv_data,})
	response.write(t.render(c))
	return response



# 대용량 CSV 스트리밍
from django.http import StreamingHttpResponse

class Echo(object):
	"""An object that implements just the write method of the file-list interface"""
	def write(self, value):
		"""Write the value by returning it, instead of storing in a buffer."""
		return value

def some_streaming_csv_view(request):
	from django.utils.six.moves import range

	# row : 대용량 DB연결로도 활용가능
	rows = (["Row {}".format(idx), str(idx)]  for idx in range(65536))  # tuple 6만줄 작업
	pseudo_buffer = Echo()
	writer = csv.writer(pseudo_buffer)
	response = StreamingHttpResponse(
		(writer.writerow(row)  for row in rows),
		 content_type="text/csv")

	response['Content-Disposition'] = 'attachment; filename="csv_file.csv"'
	return response



# PDF 생성
from reportlab.pdfgen import canvas

# canvas 로 직접 PDF 작업
def some_pdf(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="sample.pdf"'
	p = canvas.Canvas(response)               # 응답 PDF 객체를 생성한다
	p.drawString(100, 100, "Hello world.")
	p.showPage()
	p.save()
	return response


# PDF 생성 (대용량)
from io import BytesIO
from reportlab.pdfgen import canvas

def some_pdf_complex(request):
	response = HttpResponse(content_type = 'application/pdf')
	response['Content-Disposition'] = 'attachment; filename="complex.pdf"'

	# BytesIO 로 Buffer를 활용하여 PDF를 생성
	buffer = BytesIO()
	p = canvas.Canvas(buffer)
	p.drawString(100, 100, "Hello Python Django world.")
	p.showPage()
	p.save()
	pdf = buffer.getvalue()
	buffer.close()

	response.write(pdf)
	return response