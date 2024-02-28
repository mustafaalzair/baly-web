from django.db import models
from users.models import *
# Create your models here.


class Discounts(models.Model):
    vendor_name  = models.CharField( max_length=150)
    driver_name  = models.CharField( max_length=150)
    phone_number = models.CharField (max_length=150)
    created_at   = models.DateField( auto_now_add=True)
  
    def __str__(self):
        return self.vendor_name


class discount_given(models.Model):
    driver_name = models.CharField(max_length=150,default='')
    driver_phone = models.CharField(max_length=150,default='')
    vendor_name = models.CharField(max_length=150,default='')
    vendor_phone = models.CharField(max_length=150,default='')
    rating = models.CharField(max_length=150,default='')
    car = models.CharField(max_length=150,default='')
    car_color = models.CharField(max_length=150,default='')
    plate_number = models.CharField(max_length=150,default='')
    discount = models.CharField(max_length=150,default='')
    message = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.vendor_name