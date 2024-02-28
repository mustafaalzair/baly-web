from django import forms
from.models import Vendor

class LoginFrom(forms.Form):
    phone_number=forms.CharField( max_length=13)
    password=forms.CharField (max_length=50)





