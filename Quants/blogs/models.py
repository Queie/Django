# models.py의 특정 App만 반영 안될 때
# python manage.py makemigrations (yourappname)
# python manage.py migrate

from django.db import models
from django.urls import reverse
# url 경로 추출  [cf)1.11] django.core.urlresolvers


class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug  = models.SlugField(allow_unicode=True,           # 유니코드 한글처리
							max_length=100, db_index=True) # 모두 소문자 처리
	def __str__(self):
		return self.title

	def get_absolute_url(self):  # object의 canonical URL을 반환
		return reverse('blogs:category', args=(self.slug,))


# from martor.models import MartorField
from ckeditor.fields import RichTextField

class Blog(models.Model):
	# <외래키 연결> (1) on_delete = models.PROTECT (외래키 독립)
	#               (2) on_delete = models.CASCADE (외래키 의존)
	# author   = models.ForeignKey('auth.User',      on_delete=models.CASCADE )
	category = models.ForeignKey('blogs.Category', on_delete=models.CASCADE)
	title    = models.CharField(max_length=100, unique=True)
	content  = RichTextField()  # models.TextField()
	posted   = models.DateTimeField(db_index=True, auto_now_add=True)
	                                         # (1) auto_now_add : “처음생성"시간
											 # (2) auto_now     : "저장"시간
	slug     = models.SlugField(allow_unicode=True, unique=True,
							    max_length=100,  help_text='제목을 입력하세요')
	class Meta:
		ordering = ('-posted',) # 내림차순 정렬 (최신날짜 우선)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogs:post', args=(self.id,))