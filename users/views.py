from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from users.forms import UserSignUpForm, MyAuthenticationForm, ProfileForm, EditUserForm
from users.models import Profile
from product.models import Product
from merchant.forms import MerchantForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.models import Group
# Create your views here.


def home(request):
	user = request.user
	group = Group.objects.get(name='user')
	user_members = group.user_set.all()
	if user.is_authenticated:
		products = Product.objects.all()
		return render(request, 'users/home.html',{'user_members':user_members,'products':products})
	else:
		print 'sfvgb'
	return render(request, 'users/home.html')

def sign_up_check(request):
	return render(request,'users/sign_up_check.html')

def login_check(request):
	return render(request,'users/login_check.html')
def sign_up(request):
    if request.method == 'POST':
        form1 = UserSignUpForm(request.POST)
        if form1.is_valid():
            users = User.objects.create_user(username=form1.cleaned_data['username'], email=form1.cleaned_data['email'], first_name=form1.cleaned_data['first_name'], password=form1.cleaned_data['password1'], last_name=form1.cleaned_data['last_name'])
            groups = Group.objects.get(name='user')
            groups.user_set.add(users)
            return HttpResponseRedirect('/users')
    else:
        form1 = UserSignUpForm()
    variables = RequestContext(request, { 'form1': form1 })
 
    return render_to_response(
    'users/sign_up.html',
    variables,
    )

def log_in(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		user_group = User.objects.filter(groups__name='user')
		if user:
			if user in user_group:
				login(request, user)
				return HttpResponseRedirect('/users')
	else:
		form = MyAuthenticationForm()
	variables = RequestContext(request, {'form': form})
	return render_to_response('users/log_in.html',variables)

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/users')

def edit_profile(request):
    user = request.user
    users = User.objects.get(username=user)
    profile = Profile.objects.get(user=user)
    group = Group.objects.get(name='user')
    user_members = group.user_set.all()
    if user in user_members:
        if request.method == 'POST':
            form1 = EditUserForm(request.POST, instance=users)
            form2 = ProfileForm(request.POST, instance=profile)
            if form1.is_valid() and form2.is_valid():
                form2.save()
                form1.save()
                return HttpResponseRedirect('/')
        else:
     	    form1 = EditUserForm(instance=users)
       	    form2 = ProfileForm(instance=profile)
       	variables = RequestContext(request, {'user':user,'user_members':user_members,'form1': form1, 'form2':form2})
    else:
    	if request.method == 'POST':
    		form1 = MerchantForm(request.POST, instance=users)
    		if form1.is_valid():
    			form1.save()
    			return HttpResponseRedirect('/')
    	else:
    		form1 = MerchantForm(instance=users)

        variables = RequestContext(request, {'user':user,'user_members':user_members,'form1': form1})
    return render_to_response('users/edit_profile.html', variables)