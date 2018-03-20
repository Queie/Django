from django.contrib import admin

# Register your models here.
from .models import Album, Photo

class PhotoInline(admin.StackedInline):  # admin.StackedInline : 1개 파일의 요소를 세로로 나열
										 # admin.TabularInline : 가로로 나열
	model = Photo
	extra = 2                # 화면에 출력할 여유분


class AlbumAdmin(admin.ModelAdmin):
	inlines = [PhotoInline]  # PhotoInline 클래스(6번줄) 정의내용 출력
	list_display = ('name', 'description')


class PhotoAdmin(admin.ModelAdmin):
	list_display = ('title', 'upload_date')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)