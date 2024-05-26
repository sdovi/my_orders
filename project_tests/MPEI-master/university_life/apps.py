from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UniversityLifeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'university_life'
    verbose_name = _('University life')