from django.db import models

# Create your models here.
# Sqlite3 에 바로 바로 저장이 된다.

# 클래스 이름은 대문자로 시작 하는 단수형
class Candidate(models.Model):
	name = models.CharField(max_length = 10)
	introduction = models.TextField()               # 길이 제한없이 문자열 입력가능
	area = models.CharField(max_length = 15)   	    # 지역
	party_number = models.IntegerField(default = 1) # 후보 기호 (1부터 시작)

	# Candidate 클래스를 외부에 표현할 이름을 지정
	def __str__(self):
		return self.name

# 설문조사 내용 Table
class Poll(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	area = models.CharField(max_length=15)

# 투표의 결과를 저장
class Choice(models.Model):
	poll = models.ForeignKey(Poll)           # 투표종류 내용
	candidate = models.ForeignKey(Candidate) # 후보자 내용
	votes = models.IntegerField(default = 0) # 투표 결과

