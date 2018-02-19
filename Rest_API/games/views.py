from django.shortcuts import render

# Create your views here.


# Web 에서 외부의 요청시
# 1. django.http.HttpRequest 로 'request' 객체를 생성
# 2. 'request'를 views.py 의 첫 인자로 전달한다
# 3. Restful 처리를 한다 (Create, Read, Update, Delete)/(Get:검색, Post:생성)

# from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view  # Browserable API를 활용
from games.models import Game
from games.serializers import GameSerializer


# from rest_framework.renderers import JSONRenderer
# class JSONResponse(HttpResponse):
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse ,self).__init__(content, **kwargs)


# csrf_exempt : 사이트간의 위조쿠키를 생성
# 모든 게임을 나열하거나,
# 새로운 게임 데이터를 'Create' 한다
#@csrf_exempt
@api_view(['GET','POST'])
def game_list(request):
	if request.method == 'GET':       # 데이터 조회
		games = Game.objects.all()
		games_serializer = GameSerializer(games, many=True)
		# return JSONResponse(games_serializer.data)
		return Response(games_serializer.data)

	elif request.method == 'POST':    # 데이터 생성
		# game_data = JSONParser().parse(request)
		# games_serializer = GameSerializer(data = game_data)
		games_serializer  = GameSerializer(data=request.data) # 위 2줄을 1줄로 대체
		if games_serializer.is_valid():
			games_serializer.save()
			# Http 200 : 정상처리
			# return JSONResponse(games_serializer.data, status=status.HTTP_201_CREATED)
			return Response(games_serializer.data, status=status.HTTP_201_CREATED)
		# Http 400 : 정의되지 않은 작업
		# return JSONResponse(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response(games_serializer.errors, status=status.HTTP_404_BAD_REQUEST)



# pk 로 id가 특정한 대상을
# DB에서 'Read'/'Update'/'Delete' 한다
# @csrf_exempt
@api_view(['GET','PUT','POST'])
def game_detail(request, pk):
	try:       # Read, Update, Delete 객체를 선택한다
		game = Game.objects.get(pk = pk)
	except Game.DoseNotExist: # DB에 객체가 없는 경우
		# return HttpResponse(status=status.HTTP_404_NOT_FOUND)
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':  # Get 방식은 DB를 읽는다
		games_serializer = GameSerializer(game)     # game 모든 객체를 직렬화
		# return JSONResponse(games_serializer.data)  # 직렬화 객체를 JSON으로 출력
		return Response(games_serializer.data)

	elif request.method == 'PUT':
		# game_data = JSONParser().parse(request)
		# games_serializer = GameSerializer(game, data=game_data)
		games_serializer = GameSerializer(game, data=request.data) # 위 2줄을 1줄로 대체

		if games_serializer.is_valid():
			games_serializer.save()
			# return JSONResponse(games_serializer.data)
			return Response(games_serializer.data)
		# return JSONResponse(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		game.delete()
		# return HttpResponse(status=status.HTTP_204_NO_CONTENT)
		return Response(status=status.HTTP_204_NO_CONTENT)