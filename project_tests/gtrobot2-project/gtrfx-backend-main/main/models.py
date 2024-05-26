from django.db import models
from accounts.models import User


class Service(models.Model):
    SERVICE_TYPES = (
        ('crypto', 'Crypto'),
        ('forex', 'Forex'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost_usd = models.DecimalField(max_digits=10, decimal_places=2)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPES)

    def __str__(self):
        return self.name


class StoreModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')
    date_selected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name}"

