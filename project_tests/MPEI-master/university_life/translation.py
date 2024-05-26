from modeltranslation import translator
from . import models

@translator.register(models.Culture)
class CultureTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.HealthAndSport)
class HealthAndSportTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.Campus)
class CampusTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.PsycoSupport)
class PsycoSupportTranslation(translator.TranslationOptions):
    fields = ('text',)