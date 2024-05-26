from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
from ads.admin import MyTranslationAdmin

@admin.register(News)
class AdsAdmin(MyTranslationAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'id']
