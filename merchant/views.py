from django.shortcuts import render, render_to_response
from merchant.forms import MerchantSignUpForm, MerchantForm
from merchant.models import Merchant
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from users.forms import MyAuthenticationForm
from django.contrib.auth import authenticate, logout,login
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form1 = MerchantSignUpForm(request.POST)
        form2 = MerchantForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            merchant = User.objects.create_user(username=form1.cleaned_data['username'], email=form1.cleaned_data['email'], first_name=form1.cleaned_data['first_name'], password=form1.cleaned_data['password1'], last_name=form1.cleaned_data['last_name'])
            merch = Merchant(user=merchant,company=form2.cleaned_data['company'], address1=form2.cleaned_data['address1'],
            				 address2=form2.cleaned_data['address2'],address3=form2.cleaned_data['address3'],
            				 phone_number=form2.cleaned_data['phone_number'])
            merch.save()
            groups = Group.objects.get(name='merchant')
            groups.user_set.add(merchant)
            return HttpResponseRedirect('/')
    else:
        form1 = MerchantSignUpForm()
        form2 = MerchantForm()
    variables = RequestContext(request, { 'form1': form1, 'form2':form2})
 
    return render_to_response(
    'merchant/sign_up.html',
    variables,
    )

def log_in(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		user_group = User.objects.filter(groups__name='user')
		if user:
			if user not in user_group:
				login(request, user)
				return HttpResponseRedirect('/merchant')
	else:
		form = MyAuthenticationForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('merchant/log_in.html',variables)

def home(request):
	user = request.user
	group = Group.objects.get(name='user')
	user_members = group.user_set.all()
	if user.is_authenticated:
		print 'srgfrdj'
	else:
		print 'sfvgb'
	return render(request, 'merchant/home.html')