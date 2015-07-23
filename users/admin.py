from django.contrib import admin
from users.models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','place')

admin.site.register(Profile, ProfileAdmin)