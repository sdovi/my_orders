from modeltranslation import translator
from . import models

@translator.register(models.SiteLogo)
class SiteLogoTranslation(translator.TranslationOptions):
    fields = ('logo_name',)

@translator.register(models.IntroSection)
class IntroSectionTranslation(translator.TranslationOptions):
    fields = ('title', 'title2', 'title3', 'title4')

@translator.register(models.ContactAddress)
class ContactAddressTranslation(translator.TranslationOptions):
    fields = ('address',)

@translator.register(models.JoinOurNewsletterText)
class JoinOurNewsletterTextTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.Testimonials)
class TestimonialsTranslation(translator.TranslationOptions):
    fields = ('fullname', 'profession', 'text')

@translator.register(models.WhyChooseUs)
class WhyChooseUsTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.WhyChooseUsReasons)
class WhyChooseUsReasonsTranslation(translator.TranslationOptions):
    fields = ('text', 'title')

@translator.register(models.FAQs)
class FAQsTranslation(translator.TranslationOptions):
    fields = ('question', 'answer')