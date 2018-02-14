from django.contrib import admin
from profiles.models import profile
# Register your models here.


class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile, profileAdmin)