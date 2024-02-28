from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static


app_name='admins'
urlpatterns = [ 
    
    path('login_admins/',views.login_view,name='login_admin'),
    path('discount_table/',views.discount_table,name='visits'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_dashboard/drivers',views.drivers,name='drivers'),
    path('admin_dashboard/add_drivers',views.add_deiver,name='add_driver'),
    path('delete_driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
    path('admin_dashboard/delete_all_driver/', views.delete_all_driver, name='delete_all_driver'),
    path('admin_dashboard/all_vendor/', views.all_vendor, name='all_vendor'),
    path('admin_dashboard/add_vendor/', views.add_vendor, name='add_vendor'),
    path('admin_dashboard/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 