from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static
app_name='baly'


urlpatterns = [
  
    path('',views.home,name='home' ),
    path('show/<int:pk>', views.show, name='show'),
    path('showpost/<int:pk>', views.showpost, name='showpost'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 