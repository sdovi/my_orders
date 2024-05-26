from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework import generics
from .models import Info,Info_basket, Info_hokey
from .serializer import UsersSerializers, InfoBasketSerializers , InfoHokeySerializers




class Infopost(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = UsersSerializers

class Info_get_post_path(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = UsersSerializers

class Infopost_Basket(generics.ListCreateAPIView):
    queryset = Info_basket.objects.all()
    serializer_class = InfoBasketSerializers

class Info_get_post_path_Basket(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info_basket.objects.all()
    serializer_class = InfoBasketSerializers

class Infopost_Hokey(generics.ListCreateAPIView):
    queryset = Info_hokey.objects.all()
    serializer_class = InfoHokeySerializers

class Info_get_post_path_Hokey(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info_hokey.objects.all()
    serializer_class = InfoHokeySerializers




@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(username=email, email=email, password=password)
        token = Token.objects.create(user=user)
        return Response({"status": "User created", "token": token.key}, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"status": "Logged in", "token": token.key}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"status": "Logged out"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request):
    if request.auth is not None:
        user = Token.objects.get(key=request.auth.key).user
        return Response({"username": user.username, "email": user.email}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
