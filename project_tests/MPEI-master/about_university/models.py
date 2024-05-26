from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class CustomUser(User):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = _('User')
        verbose_name_plural = _('User')

class IntroduceMEI(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Introducing with MPEI")
        verbose_name_plural = _("Introducing with MPEI")


class LegalInfo(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Legal info")
        verbose_name_plural = _("Legal info")

class WEBresource(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("WEB resources")
        verbose_name_plural = _("WEB resources")

class Partners(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Partners")
        verbose_name_plural = _("Partners")

class Honorary(models.Model):
    fullname = models.CharField(max_length=150, verbose_name=_("Full name"))
    degree = models.CharField(max_length=200, verbose_name=_("Degree"))
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Honorary people")
        verbose_name_plural = _("Honorary people")


class QabulLink(models.Model):
    qabullink = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Qabul link")
        verbose_name_plural = _("Qabul link")