from django.shortcuts import render, redirect
from users.models import Vendor, Driver
from .models import Discounts
from .forms import *



def discount(request, user_id):
    user_type = request.session.get('user_type')
    vendor_id = request.session.get('vendor_id')
    
    if user_type == 'vendor':
        if request.method == 'POST':
            form = DiscountGivenForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('users:vendor_profile')
        else:
           
            form = DiscountGivenForm()
            
            
            
        driver = Driver.objects.get(user_id=user_id)
        vendor = Vendor.objects.get(id=vendor_id)
        
        if driver:
            phone_number = driver.phone_number
            
            discount = Discounts.objects.create(vendor_name=vendor, driver_name=driver, phone_number=phone_number)
        
        context = {
            'driver': driver,
            'vendor': vendor,
            'form':form,
        }
        
        return render(request, 'discount.html', context=context)
    else:
        return redirect('baly:home')