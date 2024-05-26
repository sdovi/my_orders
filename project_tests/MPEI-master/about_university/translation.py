from modeltranslation import translator
from . import models

@translator.register(models.IntroduceMEI)
class IntroduceMEITranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.LegalInfo)
class LegalInfoTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.WEBresource)
class WEBresourceTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.Partners)
class PartnersTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.Honorary)
class HonoraryTranslation(translator.TranslationOptions):
    fields = ('fullname', 'degree')
