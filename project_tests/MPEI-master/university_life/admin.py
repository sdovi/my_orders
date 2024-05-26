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



@admin.register(Culture)
class CultureAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(HealthAndSport)
class HealthAndSportAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(Campus)
class CampusAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(PsycoSupport)
class PsycoSupportAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']
