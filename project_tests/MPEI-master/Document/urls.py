from django.urls import path
from .views import *

urlpatterns = [
    path('document', Document_data, name='document'),
]
