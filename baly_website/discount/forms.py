from django import forms
from.models import *


class DiscountGivenForm(forms.ModelForm):
    class Meta:
        model = discount_given
        fields = ['driver_name', 'driver_phone', 'vendor_name', 'vendor_phone', 
                  'rating', 'car', 'car_color', 'plate_number', 'discount', 'message']