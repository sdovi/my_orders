from django.urls import path
from .views import *

urlpatterns = [
    path('conc/<str:slug>', scient_concil_view, name='scient-concil'),
    path('leaders', leaders, name='leaders'),
    path('leader-detail/<int:pk>', leader_detail, name='leader-detail'),
]
