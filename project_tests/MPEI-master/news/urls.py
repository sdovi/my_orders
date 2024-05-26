from django.urls import path
from .views import *

urlpatterns = [
    path('', newsview, name='news'),    
    path('detail/<int:pk>', news_detailview, name='news-detail'),    
]
