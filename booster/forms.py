from django import forms
from booster.models import comment,contact

                
    
class SearchForm(forms.Form):
        query = forms.CharField()


class contactForm(forms.ModelForm):
        class Meta:
                model = contact
                fields = ('name', 'email', 'company','message')