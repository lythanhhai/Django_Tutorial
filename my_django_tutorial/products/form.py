from pickle import FALSE
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="title", widget=forms.TextInput(
        attrs={
            'class': 'title_class',
            
        }
    ))
    description = forms.CharField(required=FALSE, widget=forms.Textarea(
        attrs={
            'class':  "description_class",
            'id': 'description_id',
            'rows': 15,
            'col': 50
        }
    ))
    price = forms.DecimalField(initial=199.09)
    class Meta:
        model = Product
        fields = ['title','description', 'price', 'summary', 'feature']

    # validation
    def clean_title(self, *arg, **kwarg):
        title = self.cleaned_data.get('title')
        str(title).endswith("a")
        if "1" in title:
            return title
        else:
            raise forms.ValidationError("this is a invalid title")

class ProductFormPure(forms.Form):
    title = forms.CharField(label="title", widget=forms.TextInput(
        attrs={
            'class': 'title_class',

        }
    ))
    description = forms.CharField(required=FALSE, widget=forms.Textarea(
        attrs={
            'class':  "description_class",
            'id': 'description_id',
            'rows': 15,
            'col': 50
        }
    ))
    price = forms.DecimalField(initial=199.09)