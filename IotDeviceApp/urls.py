from django.conf.urls import url
from IotDeviceApp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
  
    url(r'^parse$',views.ParseApi),
    url(r'^parse/(id=[0-9]+)$',views.ParseApi),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)