from rest_framework import serializers
from accounts.models import User

from payments.serializers import ClickOrderSerializer, YookassaOrderSerializer
from main.serializers import ServiceSerializer


class UserSerializer(serializers.ModelSerializer):
    click_order = ClickOrderSerializer(many=True)
    yookassa_order = YookassaOrderSerializer(many=True)
    services = ServiceSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'phone', 'name', 'verified', 'token', 'click_order', 'yookassa_order', 'services', 'subscription_end', 'subscription_start']