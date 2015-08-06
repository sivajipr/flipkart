from django.contrib import admin
from users.models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','place')

class AddressAdmin(admin.ModelAdmin):
	list_display = ('user','address1','address2','address3','pincode')

class BuyAdmin(admin.ModelAdmin):
	list_display = ('user','address','product','status')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Buy, BuyAdmin)