from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class Faculty(models.Model):
    name = models.CharField(max_length=255, verbose_name = _("Name"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Faculties")
        verbose_name_plural = _("Faculties")

class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name = _("Name"))
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name=_("Faculties"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Groups")
        verbose_name_plural = _("Groups")

class Schedule(models.Model):
    schedule = models.FileField(upload_to='files', verbose_name=_("Upload file"))
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_("Groups"), related_name='schedule')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self) -> str:
        return str(self.group_id)

    class Meta:
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedule")

class EduProgram(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Basic education programs")
        verbose_name_plural = _("Basic education programs")

class TreResults(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Training results")
        verbose_name_plural = _("Training results")

class AdditionalEdu(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Additional education")
        verbose_name_plural = _("Additional education")

class DistanceEdu(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Distance education")
        verbose_name_plural = _("Distance education")

class EmpAndInternship(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Employment and internship")
        verbose_name_plural = _("Employment and internship")

class FinalQua(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Final qualifiers")
        verbose_name_plural = _("Final qualifiers")

class OfficialDocs(models.Model):
    text = RichTextUploadingField(null=True, verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))

    class Meta:
        verbose_name = _("Official documents")
        verbose_name_plural = _("Official documents")
