from modeltranslation import translator
from . import models

@translator.register(models.Ads)
class AdsTranslation(translator.TranslationOptions):
    fields = ('name', 'text', 'area')

@translator.register(models.AdDetail)
class AdDetailTranslation(translator.TranslationOptions):
    fields = ('text',)