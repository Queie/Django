from django.contrib import admin
from stock.models import krxCode
# Register your models here.


class KrxAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('code',)} # slug 자동완성
    search_fields = ('code','name')  # 2개의 필드에서 색인을 사용
    # exclude = ['posted','author']
    # prepopulated_fields = {'slug': ('title',)}
    # list_filter = ('posted',)

admin.site.register(krxCode, KrxAdmin)