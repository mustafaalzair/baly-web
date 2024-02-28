from django.db import models

# Create your models here.


class Contact(models.Model):
    vendor_name=models.CharField( max_length=50)
    phone_number=models.CharField( max_length=50)
    subject=models.CharField( max_length=50)
    message=models.TextField()
    created_at = models.DateField( auto_now_add=True)