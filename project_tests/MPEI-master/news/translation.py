from modeltranslation import translator
from . import models


@translator.register(models.News)
class AdDetailTranslation(translator.TranslationOptions):
    fields = ('title', 'text',)