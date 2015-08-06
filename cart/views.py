from django.shortcuts import render
from product.models import Product
from django.contrib.auth.models import User
from cart.models import Cart
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.


@csrf_exempt
def add_to_cart(request,id):
	user = request.user
	product = Product.objects.get(id=id)
	carts = Cart.objects.all()
	if user.is_authenticated():
		if not Cart.objects.filter(user=user,product=product,status=1).exists():
			cart = Cart(user=user,product=product,status=1)
			cart.save()
			error='This item is successfully added to the cart'
			data = {'error':error}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			error='This item is already in the cart'
			flag = 1
	else:
		error = 'you need to log in first'
		flag = 1
	data = {'flag':flag, 'error':error}
	return HttpResponse(json.dumps(data), content_type="application/json")
def cart_list(request):
	user = request.user
	if user.is_authenticated():
		carts = Cart.objects.filter(user=user,status=1)
		return render(request, 'cart/cart_list.html',{'carts':carts})
	else:
		return render(request,'cart/cart_list.html')

@csrf_exempt
def remove_cart(request,id):
	cart = Cart.objects.get(id=id)
	cart.delete()
	return HttpResponse()
