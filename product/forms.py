from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
    photo = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['category'].required = True
        self.fields['selling_price'].required = True
        self.fields['original_price'].required = True
        self.fields['quantity'].required = True
        self.fields['photo'].required = True

    class Meta:
		model = Product
		exclude = ('merchant',)

class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-align','placeholder':'Title'}))
    content = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class': 'form-control form-align','placeholder':'Write your review'}))
    class Meta:
        model = Review
        fields = ('name','content')