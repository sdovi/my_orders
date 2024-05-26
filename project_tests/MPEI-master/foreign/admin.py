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


@admin.register(PreparingForeigners)
class PreparingForeignersAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(ForeignPrograms)
class ForeignProgramsAdmin(MyTranslationAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']

@admin.register(ForeignProgramDetail)
class ForeignProgramDetailAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(OrganizationCIS)
class OrganizationCISAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(Cooperation)
class CooperationAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(Graduates)
class GraduatesAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(AboutMPEIStudentsForeignPrograms)
class AboutMPEIStudentsForeignProgramsAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(Information)
class InformationAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(GlobalEnergyAssociation)
class GlobalEnergyAssociationAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(RegistrationForAMO)
class RegistrationForAMOAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']