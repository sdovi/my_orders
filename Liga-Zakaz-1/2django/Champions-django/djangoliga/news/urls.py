from django.urls import path, include
from .views import register, login_view, logout_view, get_user
from .views import Infopost, Info_get_post_path, Infopost_Basket ,Info_get_post_path_Basket, Infopost_Hokey, Info_get_post_path_Hokey



urlpatterns = [
    path('register/', register),
    path('login/', login_view),
    path('logout/', logout_view),
    path('profile/', get_user),
    path('info/<int:pk>/', Info_get_post_path.as_view()),
    path('info/', Infopost.as_view()),
    path('basket/info/<int:pk>/', Info_get_post_path_Basket.as_view()),
    path('basket/info/', Infopost_Basket.as_view()),  # Вот здесь была ошибка
    path('hokey/info/<int:pk>/', Info_get_post_path_Hokey.as_view()),
    path('hokey/info/', Infopost_Hokey.as_view()),
]
