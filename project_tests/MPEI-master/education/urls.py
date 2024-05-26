from django.urls import path
from .views import *

urlpatterns = [
    path('schedule', schedule, name='schedule'),
    path('schedule/<int:pk>', group, name='group'),
    path('edu/<str:slug>', edu, name='edu-program'),
]