from django.urls import path
from .views import IndexView
from main import views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('services/buy/', views.UserBuyService.as_view(), name='user-buy'),
]
