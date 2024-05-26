from django.urls import path

from accounts import views

urlpatterns = [
    path('get-user/', views.UserViaTokenView.as_view(), name='get-user'),
    path('user/', views.UserView.as_view(), name='user'),
    path('send-code/', views.SendCodeView.as_view(), name='send-code'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('resend-code/', views.ResendCodeView.as_view(), name='resend-code'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]