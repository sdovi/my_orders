from django.urls import path
from .views import *

urlpatterns = [
    path('', ads, name='ads'),    
    path('<int:pk>', ad_detail, name='ad_detail'),    
]
