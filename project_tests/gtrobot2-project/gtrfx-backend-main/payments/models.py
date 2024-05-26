from accounts.models import User
from django.db import models

from pyclick.models import ClickTransaction


class YookassaOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='yookassa_order')
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    paid = models.BooleanField(default=False)
    yookassa_id = models.CharField(max_length=50, null=True, blank=True, default=None)
    status = models.CharField(max_length=20, null=True, blank=True, default=None)
    recipient_account_id = models.CharField(max_length=50, null=True, blank=True, default=None)
    recipient_gateway_id = models.CharField(max_length=50, null=True, blank=True, default=None)
    yookassa_created_at = models.DateTimeField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ClickOrder(ClickTransaction):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='click_order')