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
    class Meta:
        model = Review
        fields = ('name','content')