from django.urls import path
from .views import *

urlpatterns = [
    path('<str:slug>', science_view, name='science'),
    path('event/<int:pk>', scientific_event_detail, name='science-event-detail'),
]
