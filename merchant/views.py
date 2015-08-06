from django.shortcuts import render, render_to_response
from merchant.forms import MerchantSignUpForm, MerchantForm
from merchant.models import Merchant
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from users.forms import MyAuthenticationForm
from product.models import Product
from users.models import Buy
from django.contrib.auth import authenticate, logout,login
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        form1 = MerchantSignUpForm(request.POST)
        print 1
        form2 = MerchantForm(request.POST)
        print 2
        if form1.is_valid() and form2.is_valid():
            print 3
            merchant = User.objects.create_user(username=form1.cleaned_data['username'], email=form1.cleaned_data['email'], first_name=form1.cleaned_data['first_name'], password=form1.cleaned_data['password1'], last_name=form1.cleaned_data['last_name'])
            merch = Merchant(user=merchant,company=form2.cleaned_data['company'], address1=form2.cleaned_data['address1'],
            				 address2=form2.cleaned_data['address2'],address3=form2.cleaned_data['address3'],
            				 phone_number=form2.cleaned_data['phone_number'])
            merch.save()
            groups = Group.objects.get(name='merchant')
            groups.user_set.add(merchant)
            return HttpResponse('/')
        else:
            print 'ggggggggggg'
            error='below fields are required'
            data = {"error":error}
            return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        form1 = MerchantSignUpForm()
        form2 = MerchantForm()
    variables = RequestContext(request, { 'form1': form1, 'form2':form2})
 
    return render_to_response(
    'merchant/sign_up.html',
    variables,
    )

@csrf_exempt
def log_in(request):
    print request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and User.objects.filter(groups__name='merchant',username=user.username).exists():
            login(request, user)
            return HttpResponse()
        else:
            error = 'authentication failed'
            data = {'error':error}
            return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        form = MyAuthenticationForm()
        variables = RequestContext(request, {'form': form})
    return render_to_response('merchant/log_in.html',variables)

def home(request):
	user = request.user
	group = Group.objects.get(name='user')
	user_members = group.user_set.all()
	if user.is_authenticated:
		merchant = Merchant.objects.get(user=user)
		products = Product.objects.filter(merchant=merchant)
		return render(request, 'merchant/home.html',{'products':products})
	else:
		print 'sfvgb'
		return render(request, 'merchant/home.html')

def show_product(request,p_id):
	product = Product.objects.get(id=p_id)
	buy = Buy.objects.filter(product=product)
	return render(request,'merchant/show_product.html',{'product':product,'buys':buy})