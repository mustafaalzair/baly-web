from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.models import Vendor


class CustomLoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # تخصيص إذا لزم الأمر

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    is_staff = forms.BooleanField(required=False, help_text='Mark if the user should be a staff member.')
    is_superuser = forms.BooleanField(required=False, help_text='Mark if the user should be a superuser.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')
        
        
class Add_vendor(forms.ModelForm):
     class Meta:
        model = Vendor
        fields = ['vendor', 'password', 'title', 'subtitle', 
                  'description', 'image', 'link', 'phone_number', 'city','Sub_Category']
    