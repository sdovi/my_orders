from modeltranslation import translator
from . import models

@translator.register(models.ResearchAndDev)
class ResearchAndDevTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.ScientInfrastructure)
class ScientInfrastructureTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.ScientificCert)
class ScientificCertTranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.Journals)
class JournalsTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.ScientEvents)
class ScientEventsTranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.ScientEventDetail)
class ScientEventDetailTranslation(translator.TranslationOptions):
    fields = ('text',)