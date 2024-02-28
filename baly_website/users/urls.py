from django.urls import path
from . import views
from.views import login,logout_view
from django.conf import settings
from django.conf.urls.static import static
app_name = 'users'


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('driver/', views.drivers, name='driver_profile'),  
    path('vendor_profile/', views.vendor_profile, name='vendor_profile'),  
    path('qr_code/', views.qr_code, name='driver_QRcode'),
    path('vendors/', views.all_vendors, name='all_vendors'),
    path('offer/<str:user_id>', views.offer_vendor, name='offer_vendor'),
    path('Terms_and_conditions/<int:pk>', views.Terms_and_conditions, name='Terms_and_conditions'),
  
]+static(settings.MEDIA_URL, document_root=settings.BASE_DIR)


