from django.shortcuts import render,render_to_response
from product.forms import ProductForm
from product.models import Product
from merchant.models import Merchant
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

def add_product(request):
	user = request.user
	print request
	merchant = Merchant.objects.get(user=user)
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			print form.cleaned_data['photo']
			product = Product(merchant=merchant,name=form.cleaned_data['name'],
							  category=form.cleaned_data['category'],
							  selling_price=form.cleaned_data['selling_price'],
							  original_price=form.cleaned_data['original_price'],
							  quantity=form.cleaned_data['quantity'],
							  photo = request.FILES['photo'])
			product.save()
		return HttpResponseRedirect('/merchant')
	else:
		form = ProductForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('product/add_product.html', variables)

def show_product(request,id):
	product = Product.objects.get(id=id)
	return render(request,'product/show_product.html',{'product':product})