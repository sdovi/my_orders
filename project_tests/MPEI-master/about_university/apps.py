from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AboutUniversityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_university'
    verbose_name = _("about_university")
