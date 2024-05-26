from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ForeignConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foreign'
    verbose_name = _('International activity')