from rest_framework import serializers
from .models import Info_email, Info_article

class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info_email
        fields = '__all__'

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info_article
        fields = '__all__'
