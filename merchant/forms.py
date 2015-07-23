from django import forms
from django.contrib.auth.models import User
from merchant.models import *

class MerchantSignUpForm(forms.Form):
	username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Username'}))
	first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Firstname'}))
	last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Lastname'}))
 	email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Email'}))
 	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-align','placeholder':'Password'}), max_length=50)
 	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-align','placeholder':'Re enter password'}), max_length=50)
 	def clean_username(self):
 		try:
 			user = User.objects.get(username__iexact=self.cleaned_data['username'])
 		except User.DoesNotExist:
 			return self.cleaned_data['username']
 		raise forms.ValidationError('The user already exists')

 	def clean(self):
 		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
 			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
 				raise forms.ValidationError('passwords does not match')
 			else:
 				return self.cleaned_data

class MerchantForm(forms.ModelForm):
	company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Username'}))
	address1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Username'}))
	address2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Username'}))
	address3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Username'}))
	phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Username'}))
	class Meta:
		model = Merchant
		fields = ('company', 'address1', 'address2','address3','phone_number')

