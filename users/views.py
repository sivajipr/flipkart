from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from users.forms import UserSignUpForm, AddressForm, MyAuthenticationForm, ProfileForm, EditUserForm
from users.models import Profile, Address, Buy
from product.models import Product
from merchant.models import Merchant
from merchant.forms import MerchantForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.models import Group
from django.core.mail import send_mail
import base64
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
# Create your views here.


def home(request):
    user = request.user
    group = Group.objects.get(name='user')
    user_members = group.user_set.all()
    if user.is_authenticated():
        products = Product.objects.all()
        return render(request, 'users/home.html',{'user_members':user_members,'products':products})
    else:
        products = Product.objects.all()
        return render(request, 'users/home.html',{'products':products})

def sign_up_check(request):
    products = Product.objects.all()
    return render(request,'users/sign_up_check.html',{'products':products})

def login_check(request):
    products = Product.objects.all()
    return render(request,'users/login_check.html',{'products':products})

def sign_up(request):
    if request.method == 'POST':
        form1 = UserSignUpForm(request.POST)
        if form1.is_valid():
            users = User.objects.create_user(username=form1.cleaned_data['username'], email=form1.cleaned_data['email'], first_name=form1.cleaned_data['first_name'], password=form1.cleaned_data['password1'], last_name=form1.cleaned_data['last_name'])
            groups = Group.objects.get(name='user')
            groups.user_set.add(users)
            user = authenticate(username=form1.cleaned_data['username'], password=form1.cleaned_data['password1'])
            login(request, user)
            return HttpResponse()
        else:
            error='below fields are required'
            data = {'error':error}
            return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        form1 = UserSignUpForm()
    variables = RequestContext(request, { 'form1': form1 })
 
    return render_to_response(
    'users/sign_up.html',
    variables,
    )

@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username:
            if password:
                user = authenticate(username=username, password=password)
                user_group = User.objects.filter(groups__name='user')
                if user:
                    if user in user_group:
                        login(request, user)
                        return HttpResponse()
                else:
                    error = 'username or password is not correct'
                    data = {'error':error}
                    return HttpResponse(json.dumps(data), content_type="application/json")
            else:
                error = 'Password is required'
                data = {'error':error}
                return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            error = 'username is required'
            data = {'error':error}
            return HttpResponse(json.dumps(data), content_type="application/json")

    else:
        form = MyAuthenticationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('users/login_popup.html',variables)

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

def forget_password(request):
    if request.method == 'POST':
        em=request.POST.get('email')
        user = User.objects.get(email=em)
        encrypt_string = base64.encodestring(user.username)
        url = request.META["HTTP_HOST"]+'/users/newpassword/'+encrypt_string
        send_mail('forget password', 'Reset the password of your flipkart account '+ url, 'sivaji@sparksupport.com',
        [em],fail_silently=False)
        message='A password reset url is send to your email'
        return render(request, 'users/forgetpassword.html',{'message':message})

    else:
        return render(request,'users/forgetpassword.html')

def new_password(request,user):
    decrypt_string = base64.decodestring(user)
    real_user = User.objects.get(username=decrypt_string)
    if request.method == 'POST':
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            real_user.set_password(pass1)
            real_user.save()
            return HttpResponseRedirect('/users/login')
        else:
            message = 'password does not match'
            return render(request,'users/newpassword.html',{'message':message})
    else:
        return render(request,'users/newpassword.html',{'user':user})

def address_verify(request,id):
    user = request.user
    product = Product.objects.get(id=id)
    addreses = Address.objects.filter(user=request.user)
    if user.is_authenticated():
        if request.method == 'POST':
            form = AddressForm(request.POST)
            if form.is_valid():
               address = Address(user=request.user, address1=form.cleaned_data['address1'],
                                 address2=form.cleaned_data['address2'],
                                 address3=form.cleaned_data['address3'],
                                 pincode=form.cleaned_data['pincode'],
                                 phone_number=form.cleaned_data['phone_number'])
               address.save()
               return HttpResponseRedirect("/users/address-verify/%d"% int(id))
                
        else:
            form = AddressForm()
            return render(request, "users/address_verify.html",{'id':id, 'addreses':addreses,'form':form})
    else:
        return render(request,'users/login_popup.html')

def address_delete(request,id):
    address = Address.objects.get(id=id)
    address.delete()
    return HttpResponseRedirect("/users/address-verify/%d"% int(id))

def login_popup(request):
    form = MyAuthenticationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('users/login_popup.html',variables)

def signup_popup(request):
    form1 = UserSignUpForm()
    form2 = MerchantForm()
    variables = RequestContext(request, {'form1': form1,'form2':form2})
    return render_to_response('users/signup_popup.html',variables)

def buyed_products(request):
    user = request.user
    buys = Buy.objects.filter(user=user,status=1)
    return render(request,'users/purchased.html',{'buys':buys})

def usersearch(request):
    name = request.GET['name']
    products = Product.objects.filter(name__icontains=name)
    return render(request,'users/usersearch.html',{'products':products, 'name':name})

def auto_complete(request):
    data=[]
    term = request.GET['term']
    products = Product.objects.filter(Q(name__icontains=term)|Q(category__icontains=term))
    for product in products:
        d={}
        d['label'] = product.name
        d['id'] = product.id
        data.append(d)
    return HttpResponse(json.dumps(data), content_type="application/json")