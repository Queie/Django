from django.db import models

# Create your models here.


# id 컬럼의 pk 값들은 django 에서 자동으로 생성해준다
class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

# id 컬럼의 pk 값들은 django 에서 자동으로 생성해준다
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length= 200)
	votes = models.IntegerField(default = 0)