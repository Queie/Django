from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

from stock.models import krxCode
from stock.sqlite import sqlite_table, stocks_38new

# 개별 code의 페이지 구성하기
def codes(request, slug):
	krx = get_object_or_404(krxCode, slug=slug)
	code = krx.code

	# import sqlite3  # 현재작업 : './Quants/'' 기본폴더를 기준
	# (1) DataFrame : .to_html() 메서드로 출력한다
	table = sqlite_table('./IPython/data/krxStock.db')
	# table = stocks_38new()  # 신규 상장목록

	# (2) [list] 는 template에서 for 문으로 활용
	temp = [1,2,3,4,5]
	print(type(krx.code_gogl), code)
	return render(request, 'stock/codes.html', {'codes':krx, 'temp':temp, 'table':table})
	# return HttpResponse(krx_db)
	# Blog.objects.filter(title__icontains=q)




def index(request):
	return HttpResponse("Stock Sites")
