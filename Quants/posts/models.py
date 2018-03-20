from django.db import models
# Create your models here.

from django.urls import reverse
from tagging.fields import TagField

from django.contrib.auth.models import User
from django.utils.text  import slugify  # slug 를 생성


class Post(models.Model):
	title = models.CharField('TITLE', max_length=50) # 컬럼명 정의
	slug  = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title')
	description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
	content     = models.TextField('CONTENT')
	create_date = models.DateTimeField('Create Date', auto_now_add=True)
	modify_date = models.DateTimeField('Modify Date', auto_now=True)
	tag = TagField()

	# ForeignKey() 항상 on_delete를 정의해야 한다
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name='post'
		verbose_name_plural = 'posts'   # html 에서 for 반복시 복수형
		db_table = 'my_post'            # 테이블 이름
		ordering = ('-modify_date',)

	def __str__(self):
		return self.title               # title 필드를 출력

	def get_url(self):
		return reverse('post:post_detail', args=(self.slug,))

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title, allow_unicode=True)
		super(Post, self).save(*args, **kwargs)