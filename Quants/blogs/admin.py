from django.contrib import admin
from blogs.models import Category, Blog
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # slug 자동완성


# from pagedown.widgets import AdminPagedownWidget
# from django.db import models

# class BlogAdmin(admin.ModelAdmin):
#     exclude = ['posted','author']
#     prepopulated_fields = {'slug': ('title',)}
#     list_filter = ('posted',)
#     search_fields = ('title','content')
#     formfield_overrides = {
#         models.TextField: {'widget': AdminPagedownWidget },
#     }

from martor.widgets import AdminMartorWidget
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted','author']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('posted',)
    search_fields = ('title','content')
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

# model을 그대로 admin 활용 (단 slug 자동완성은 X)
# admin.site.register(Blog)
# admin.site.register(Category)