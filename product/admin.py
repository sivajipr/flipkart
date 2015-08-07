from django.contrib import admin
from product.models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ('merchant','name','category','selling_price','quantity','photo')
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('user','product','name','content')

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)