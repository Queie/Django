from django.db import models

# Create your models here.
from django.urls import reverse
from .fields import ThumbnailImageField

class Album(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField('One Line Description', max_length=100, blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_url(self):
		return reverse('photo:album_detail', args=(self.id,))


class Photo(models.Model):

	#  .ForeignKey(  ,on_delete=models.CASCADE) : 기본키 삭제시, 종속키들도 삭제
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	image = ThumbnailImageField(upload_to='photo %Y %m')
	description = models.TextField('Photo Description', blank=True)
	upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title

	def get_url(self):
		return reverse('photo:index', args=(self.id,))
