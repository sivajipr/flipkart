from django.shortcuts import render
from product.models import Product
from django.contrib.auth.models import User
from cart.models import Cart
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def add_to_cart(request,id):
	user = request.user
	product = Product.objects.get(id=id)
	carts = Cart.objects.all()
	if not Cart.objects.filter(user=user,product=product,status=1).exists():
		cart = Cart(user=user,product=product,status=1)
		cart.save()
	return HttpResponseRedirect('/product/%d'% product.id)

def cart_list(request):
	user = request.user
	carts = Cart.objects.filter(user=user,status=1)
	return render(request, 'cart/cart_list.html',{'carts':carts})