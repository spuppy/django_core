from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	class meta:
		name = Profile

admin.site.register(Profile,ProfileAdmin)