from django.urls import path
from .views import *

urlpatterns = [
    path('news/create', news_add, name='news-add'),    
]