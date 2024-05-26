from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class Ads(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    text = models.TextField(null=True, verbose_name=_('Text'))
    period = models.DateField(null=True, verbose_name=_('period'))
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    count = models.IntegerField(default=0, null=True, verbose_name=_('count'))
    area = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('area'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Ads")
        verbose_name_plural = _("Ads")

class AdDetail(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    ad_id = models.ForeignKey(Ads, on_delete=models.CASCADE, verbose_name=_('Ad'), null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Ad detail")
        verbose_name_plural = _("Ad detail")
