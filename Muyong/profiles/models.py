from django.db import models

# Create your models here.

class profile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default='description default text')
	# location = models.CharField(max_length=120, default='my location default', blank=True, null=True)
	# job = models.CharField(max_length=120, null=True) # (null=True) 빈칸도 데이터 허용

	def __str__(self):
		return self.name
