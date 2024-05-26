from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ScienceAndInnovationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'science_and_innovation'
    verbose_name = _("Science and Innovation")
