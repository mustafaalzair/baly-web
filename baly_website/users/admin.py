# Register your models here.
from django.contrib import admin
from .models import Vendor, Driver


@admin.register(Vendor)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['vendor'] # عرض حقول الهاتف ورقم الهوية في قائمة البائعين
    # يمكنك إضافة حقول إضافية للعرض في القائمة
    
    
@admin.register(Driver)
class CaptainAdmin(admin.ModelAdmin):
    list_display =['phone_number']  # عرض حقول الهاتف ورقم الهوية في قائمة الكباتن
    # يمكنك إضافة حقول إضافية للعرض في القائمة
    
