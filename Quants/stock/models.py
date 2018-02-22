from django.db import models
from django.urls import reverse # 개별 Code 의 DashBoard 만들기
# Create your models here.


class krxCode(models.Model):
	name = models.CharField(max_length=20, db_index=True)
	code = models.CharField(max_length=10, db_index=True)
	code_gogl = models.CharField(max_length=20, db_index=True)

	# 색인용 slug : 별도로 이를 설정하면 url 이동에 유리
	slug  = models.SlugField(max_length=10, db_index=True)

	# 대표 출력명 (admin, get_object_or_404(), .get())
	# cf) object.필드명 : 개별 필드 내용을 string 출력
	def __str__(self):
		return u'%s %s'%(self.code, self.name)

	# def get_absolute_url(self):
	# 	return reverse('stock:dashboard', args=(self.code,)) # Code명을 사용하여 구분