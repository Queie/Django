# 내가 부족한 부분
# 1. form 다루기
# 2. form 을 활용하여 DB를 편집 - 테이블 수정

from django import forms

class SearchForm(forms.Form):
	search_word = forms.CharField(label='검색')
	# search_word : form 에서 생성/전달 객체를 정의
	# label =     : Web 표시내용
	# search.html 의 10줄에 삽입되는 객체 {{form.as_table}}