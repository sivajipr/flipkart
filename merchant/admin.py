from django.contrib import admin
from merchant.models import *
# Register your models here.
class MerchantAdmin(admin.ModelAdmin):
	list_display = ('user','company','address1','address2','address3')

admin.site.register(Merchant, MerchantAdmin)