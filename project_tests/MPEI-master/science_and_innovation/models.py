from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class ResearchAndDev(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Research and development")
        verbose_name_plural = _("Research and development")

class ScientInfrastructure(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Scientific infrastructure")
        verbose_name_plural = _("Scientific infrastructure")

class ScientificCert(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("State scientific certificate")
        verbose_name_plural = _("State scientific certificate")

class Journals(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Journals")
        verbose_name_plural = _("Journals")

class ScientEvents(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = _("Scientific events")
        verbose_name_plural = _("Scientific events")

class ScientEventDetail(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    scientevent_id = models.ForeignKey(ScientEvents, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Scientific event detail")
        verbose_name_plural = _("Scientific event detail")