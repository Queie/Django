# Custom Field 파이썬 파일
# > thumbnail 이미지 생성

from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os


# thumb 파일이름 생성
def _add_thumb(s):
	parts = s.split(".")
	parts.insert(-1, "thumb")
	if parts[-1].lower() not in ['jpeg', 'jpg']:
		parts[-1] = 'jpg'
	return ".".join(parts)


# image 생성
# Decorator : 함수 내 지역변수를 외부에서 제어
class ThumbnailImageFieldFile(ImageFieldFile):

	def _get_thumb_path(self):
		return _add_thumb(self.path)

	def _get_thumb_url(self):
		return _add_thumb(self.url)

	# _get_thumb_path 받은 self(Request URL) 추출
	thumb_path = property(_get_thumb_path)
	thumb_url  = property(_get_thumb_url)

	def save(self, name, content, save=True):
		super(ThumbnailImageFieldFile, self).save(name, content, save)
		img = Image.open(self.path)
		size = (128, 128)
		img.thumbnail(size, Image.ANTIALIAS)
		background = Image.new('RGBA', size, (255, 255, 255, 0))
		background.paste(
			img, ( int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2) ) )
		background.save(self.thumb_path, 'JPEG')


	# PIL 모듈로 썸네일 만들기
	# https://webisfree.com/2017-08-01/python-%EC%9D%B4%EB%AF%B8%EC%A7%80-resize-thumbnail-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0
	# def save(self, name, content, save=True):
	# 	super(ThumbnailImageFieldFile, self).save(name, content, save)
	# 	img = Image.open(self.path)
	# 	size = (128,128)
	# 	img.thumbnail(size, Image.ANTIALIAS)
	# 	background = Image.new('RGBA', size, (255,255,255,0))
	# 	background.paste(img, (int((size[0] - img.size[0])/2), int((size[1]-img.size[1])/2) ))
	# 	background.save(self.thumb_path, 'JPEG')



	def delete(self, save=True):
		if os.path.exists(self.thumb_path):
			os.remove(self.thumb_path)
		super(ThumbnailImageFieldFile, self).delete(save)


class ThumbnailImageField(ImageField):
	attr_class = ThumbnailImageFieldFile

	def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):

		# @property 로 추출한 매개변수를 활용
		self.thumb_width  = thumb_width
		self.thumb_height = thumb_height
		super(ThumbnailImageField, self).__init__(*args, **kwargs)