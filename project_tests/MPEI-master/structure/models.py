from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class ScientificCouncil(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    academic_degree = models.CharField(max_length=200, verbose_name=_("Academic degree"))
    about = models.CharField(max_length=255, verbose_name=_("About"), null=True)
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Scientific Council")
        verbose_name_plural = _("Scientific Council")

class UniversityManagement(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("University management")
        verbose_name_plural = _("University management")

class MPEIuzLeaders(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    academic_degree = models.CharField(max_length=200, verbose_name=_("Academic degree"))
    some_text = models.CharField(max_length=255, verbose_name=_('Some text'), null=True)
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone number'), null=True)
    email = models.CharField(max_length=150, verbose_name=_('Email'), null=True)
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Heads of MPEI Tashkent branch")
        verbose_name_plural = _("Heads of MPEI Tashkent branch")

class MPEIuzLeaderDetail(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    mpeiuzLeaders_id = models.ForeignKey(MPEIuzLeaders, on_delete=models.CASCADE, verbose_name=_("Heads of MPEI Tashkent branch"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Head detail of MPEI Tashkent branch")
        verbose_name_plural = _("Head detail of MPEI Tashkent branch")

class TheBoardOfDirectors(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    academic_degree = models.CharField(max_length=200, verbose_name=_("Academic degree"))
    position = models.CharField(max_length=200, verbose_name=_("Position"))
    image = models.ImageField(upload_to='images', verbose_name=_("image"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("The board of directors")
        verbose_name_plural = _("The board of directors")

class DepartmentsAndCenters(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Departments and centers of MPEI")
        verbose_name_plural = _("Departments and centers of MPEI")

class OfficesAndDepartments(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Offices and departments of MPEI")
        verbose_name_plural = _("Offices and departments of MPEI")

class PublicOrganizations(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Public organizations")
        verbose_name_plural = _("Public organizations")

