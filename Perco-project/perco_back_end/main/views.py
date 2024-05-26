from django.shortcuts import render
from .serializer import EmailSerializers, ArticleSerializers
from rest_framework import generics
from .models import Info_email, Info_article

class email(generics.ListCreateAPIView):
    queryset = Info_email.objects.all()
    serializer_class = EmailSerializers

class article(generics.ListCreateAPIView):
    queryset = Info_article.objects.all()
    serializer_class = ArticleSerializers
