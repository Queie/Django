from django.contrib import admin
# models.py 에 정의한 내용을 admin 에서 사용
from .models import Candidate, Poll, Choice


# Register your models here .
# /admin 에서 관리할 목록을 직접 연결한다
admin.site.register(Candidate)
admin.site.register(Poll)
admin.site.register(Choice)