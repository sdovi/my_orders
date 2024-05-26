from django.urls import path
from .views import *

urlpatterns = [
    path('<str:slug>', about_university_view, name='about_university'),
]
