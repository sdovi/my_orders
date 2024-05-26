from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)

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

@admin.register(IntroduceMEI)
class IntroduceMEIAdmin(MyTranslationAdmin):
    list_display = ['id', 'created_at']
    search_fields = ['text', 'id']

@admin.register(LegalInfo)
class LegalInfoAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(WEBresource)
class WEBresourceAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(Partners)
class PartnersAdmin(MyTranslationAdmin):
    list_display = ['id', 'text']
    search_fields = ['text', 'id']

@admin.register(Honorary)
class HonoraryAdmin(MyTranslationAdmin):
    list_display = ['id', 'fullname']
    search_fields = ['fullname', 'id']

@admin.register(QabulLink)
class QabulLinkAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

