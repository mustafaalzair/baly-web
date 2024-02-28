from django import forms
from .models import Contact



class Formcontact(forms.ModelForm):
    class Meta:
        model=Contact
        fields =['vendor_name','phone_number','subject','message']