from django.urls import path, include
from .views import email, article



urlpatterns = [
    path('email/', email.as_view()),
    path('article/', article.as_view()),
]
