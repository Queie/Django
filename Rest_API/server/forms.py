# form을 django를 사용하여 생성
from django import forms

class ContactForm(forms.Form):

	subject = forms.CharField(max_length=100)        # 입력가능 최대길이
	email = forms.EmailField(required=False,         # 선택적 입력사항
	                         label='to e-mail')
	message = forms.CharField(widget=forms.Textarea) # text 입력창 활용

	# clean_필드이름  : 자동으로 message  필드의 유표성 검사를 실행
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())

		if num_words < 4:  # 전체 단어가 4개 미만일 떄
			raise forms.ValidationError("Not enough words!")  # 폼에 오류를 표시
		print(message)
		return message