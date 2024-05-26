from django.urls import path
from .views import *

urlpatterns = [
    path('international/<str:slug>', international_view, name='international'),
    path('program/<int:pk>', foreign_program_detail, name='foreign-program-detail'),
]