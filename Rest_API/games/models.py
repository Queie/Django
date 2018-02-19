from django.db import models

# Create your models here.

# 게임의 Category를 관리하는 model을 정의
class GameCategory(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name


# 게임을 관리하는 model을 정의
class Game(models.Model):
	created = models.DateTimeField(auto_now_add = True)
	name = models.CharField(max_length=200, blank=True ,default='')
	release_date = models.DateTimeField()
	# game_category = models.CharField(max_length=200, blank=True, default='')
	game_category = models.ForeignKey(GameCategory,
		                              related_name='games',     # 역방향의 관계를 만든다
		                              on_delete=models.CASCADE) # 기본키 삭제시, 종속내용도 삭제
	# django2.0 추가 (외래키 독립) : 기본키와 별도로 DB가 남는다
	played = models.BooleanField(default=False)

	# DB 출력시, 'name'필드의 알파벳 순서로 정렬
	class Meta:
		ordering = ('name',)

	# admin의 출력이름을 지정
	def __str__(self):
		return self.name


# 점수를 기록할 사용자 정보 DB
class Player(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),)
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50, blank=False, default='')
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE,)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name


# Player의 점수 DB
class PlayerScore(models.Model):        # Q) 왜 여기선 복수인가??
	player = models.ForeignKey(Player, related_name='scores',on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	score = models.IntegerField()
	score_date = models.DateTimeField()

	class Meta:
		ordering = ('-score',)