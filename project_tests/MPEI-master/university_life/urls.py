from django.urls import path
from .views import *

urlpatterns = [
    path('life/<str:slug>', univer_life_view, name='univer-life'),
]
