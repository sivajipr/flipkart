from django.contrib import admin
from cart.models import *
# Register your models here.
class CartAdmin(admin.ModelAdmin):
	list_display = ('user','product','status')

admin.site.register(Cart, CartAdmin)