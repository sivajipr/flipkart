from django.shortcuts import render,render_to_response
from product.forms import ProductForm, ReviewForm
from product.models import Product, Review
from merchant.models import Merchant
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from users.models import Address, Buy
from users.forms import BuyForm
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def add_product(request):
	user = request.user
	merchant = Merchant.objects.get(user=user)
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = Product(merchant=merchant,name=form.cleaned_data['name'],
							  category=form.cleaned_data['category'],
							  selling_price=form.cleaned_data['selling_price'],
							  original_price=form.cleaned_data['original_price'],
							  quantity=form.cleaned_data['quantity'],
							  photo = request.FILES['photo'])
			product.save()
			return HttpResponseRedirect('/merchant')

		else:
			pass
	else:
		form = ProductForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('product/add_product.html', variables)

def show_product(request,id):
	product = Product.objects.get(id=id)
	return render(request,'product/show_product.html',{'product':product})

def buy_product(request, address_id, product_id):
	user = request.user
	address = Address.objects.get(id=address_id)
	product = Product.objects.get(id=product_id)
	if request.method =='POST':
		form = BuyForm(request.POST)
		print form
		if (product.quantity-form.cleaned_data['quantity'])>=0:
			product.quantity = product.quantity-form.cleaned_data['quantity']
			buy = Buy(user=user, address=address,product=product,status=1, quantity=form.cleaned_data['quantity'])
			buy.save()
			product.save()
			return HttpResponse()
		else:
			error = '%d pieces are not available' %form.cleaned_data['quantity']
			data = {'error':error}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		form = BuyForm()
	variables = RequestContext(request, {'form': form, 'product':product,'address':address})
	return render_to_response('product/buy_conform.html', variables)

@csrf_exempt
def buyerror(request,id):
	print 'assssssssssssss'
	error = 'This item is not available'
	data = {'error':error}
	return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def review_write(request,id):
	user=request.user
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			print 'ssssssssssssssss'
			review = Review(name=form.cleaned_data['name'],content = form.cleaned_data['content'],
							user=user,product=product)
			print 'bbbbbbbbbbbb'
			review.save()
			print'qqqqqqqq'
			return HttpResponse()
		else:
			error = 'please write something'
			data = {'error':error}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		form = ReviewForm()
	variables = RequestContext(request, {'form': form, 'product':product})
	return render_to_response('product/review_write.html', variables)

def review_show(request,id):
	print 1
	product = Product.objects.get(id=id)
	print 2
	reviews = product.review_set.all()
	print 3
	return render(request,'product/review_show.html',{'reviews':reviews})


