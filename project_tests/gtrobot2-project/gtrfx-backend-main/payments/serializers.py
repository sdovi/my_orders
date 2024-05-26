from rest_framework import serializers
from .models import ClickOrder
from rest_framework import serializers
from .models import YookassaOrder, ClickOrder


class YookassaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = YookassaOrder
        fields = (
            'id',
            'status',
            'amount',
            'paid',
            'yookassa_id',
            'created_at',
        )

class ClickOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickOrder
        fields = (
            'id',
            'status',
            'amount',
            'click_paydoc_id',
            'created',
            'message',
        )
