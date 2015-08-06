from django.contrib import admin
from product.models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ('merchant','name','category','selling_price','quantity','photo')

admin.site.register(Product, ProductAdmin)