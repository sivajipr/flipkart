from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
	photo = forms.FileField()
	class Meta:
		model = Product
		exclude = ('merchant',)