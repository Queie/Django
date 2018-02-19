# Restful API를 위한, 직렬화 역직렬화 관리
# : 실시간 연동 않고서도, Json으로 입력(Post)과 출력(Get)이 가능
# https://www.youtube.com/watch?v=xUMURjoPddY    # restAPI의 개념설명
from rest_framework import serializers
from games.models import Game


# Restful API 작업할 필드의 속성을 정의한다
# 직렬화 필드의 Rest '서브 클래스'를 선언한다
# 수동으로 매핑한 속성을 선언하고 메서드 들을 Overwriting 한다
# cf) class Game 중 'created' 컬럼은 제외하고 연결
class GameSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=200)   # max_length : 전달정보 값
	release_date = serializers.DateTimeField()

	game_category = serializers.CharField(max_length=200)
	played = serializers.BooleanField(required=False)

	# .save() 메서드 호출시 활성화 1 (새로저장)
	# NotImplaementdError 예외를 발생하지 않아서 class 내부에 정의
	def create(self, validated_data):
		return Game.objects.create(**validated_data)

	# .save() 메서드 호출시 활성화 2 (기존자료 갱신)
	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.release_date = validated_data.get('release_date', instance.release_date)
		instance.game_category = validated_data('game_category', instance.game_category)
		instance.played = validated_data('played', instance.played)
		instance.save()
		return instance

	class Meta:
		model = Game
		fields = ('id',
				  'name',
				  'game_category',
				  'release_date',
				  'played')