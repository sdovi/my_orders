from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class PreparingForeigners(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Preparing foreigners")
        verbose_name_plural = _("Preparing foreigners")

class ForeignPrograms(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Foreign Programs")
        verbose_name_plural = _("Foreign Programs")

class ForeignProgramDetail(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    foreignprograms_id = models.ForeignKey(ForeignPrograms, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Foreign Program detail")
        verbose_name_plural = _("Foreign Program detail")

class OrganizationCIS(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("The main organization of the CIS")
        verbose_name_plural = _("The main organization of the CIS")

class Cooperation(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Cooperation")
        verbose_name_plural = _("Cooperation")
        
class Graduates(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Graduates")
        verbose_name_plural = _("Graduates")

class AboutMPEIStudentsForeignPrograms(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Foreign Programs of Students of MPEI")
        verbose_name_plural = _("Foreign Programs of Students of MPEI")

class Information(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Information")
        verbose_name_plural = _("Information")

class GlobalEnergyAssociation(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Global Energy Association")
        verbose_name_plural = _("Global Energy Association")

class RegistrationForAMO(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Registration form for participants of the 25th anniversary conference of AMO")
        verbose_name_plural = _("Registration form for participants of the 25th anniversary conference of AMO")




