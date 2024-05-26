from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager


class User(AbstractUser):
    username = None
    email = None
    first_name = None
    last_name = None
    phone = models.CharField(_("Phone number"), max_length=15, unique=True)

    name = models.CharField(_("Name"), max_length=255, blank=True, null=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    verified = models.BooleanField(default=False)

    token = models.CharField(max_length=255, null=True, blank=True, default=None)
    token_is_used = models.BooleanField(default=False)

    subscription_start = models.DateTimeField(blank=True, null=True, default=None)
    subscription_day = models.IntegerField(default=0)
    subscription_end = models.DateTimeField(blank=True, null=True, default=None)

    services = models.ManyToManyField("main.Service", related_name="users", blank=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class UserVerification(models.Model):
    SENT_VIA_CHOICES = (('sms', 'SMS'), ('whatsapp', 'Whatsapp'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    sent_via = models.CharField(max_length=10, choices=SENT_VIA_CHOICES, default='sms')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.phone} - {self.code}"
