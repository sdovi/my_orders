from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ResearchAndDev)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(ScientInfrastructure)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(ScientificCert)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']

@admin.register(Journals)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(ScientEvents)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']

@admin.register(ScientEventDetail)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']