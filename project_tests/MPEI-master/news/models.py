from django.db import models
from django.utils.translation import gettext_lazy as _

class News(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name=_('Title'))
    text = models.TextField(null=True, verbose_name=_('Text'))
    count = models.IntegerField(default=0, null=True, verbose_name=_('count'))
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    image_extra1 = models.ImageField(upload_to='images', verbose_name=_("image"), blank=True)
    image_extra2 = models.ImageField(upload_to='images', verbose_name=_("image"), blank=True)
    image_extra3 = models.ImageField(upload_to='images', verbose_name=_("image"), blank=True)
    image_extra4 = models.ImageField(upload_to='images', verbose_name=_("image"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

