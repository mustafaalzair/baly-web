from django.db import models
from datetime import datetime
import secrets



def generate_random_id_vendor():
    
    return ''.join(secrets.choice('1234567890abc') for _ in range(5))



class Vendor(models.Model):
    vendor = models.CharField(max_length=50)
    password=models.CharField( max_length=50,)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    link = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)
    city = models.CharField(max_length=120, default='بغداد')
    Sub_Category = models.CharField(max_length=120, default='')
    created_at = models.DateField( auto_now_add=True,null=True)
    user_id=models.CharField( max_length=5,default=generate_random_id_vendor,unique=True)
    
    
    def __str__(self):
        return self.vendor
    
    
    

def generate_random_id():
    #It creates a user ID for each driver to use in QR code
    return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*0123456789') for _ in range(15))


class Driver(models.Model):
       
    full_name = models.CharField(max_length=75)
    rating = models.CharField(max_length=50)
    password=models.CharField( max_length=50,)
    car = models.CharField(max_length=50)
    color_car = models.CharField(max_length=25)
    plate_number = models.CharField(max_length=8)
    
    phone_number = models.CharField(max_length=13)
    
    user_id=models.CharField( max_length=15,default=generate_random_id,unique=True)
    
    def __str__(self):
        return self.full_name