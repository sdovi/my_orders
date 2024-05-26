from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import User, UserVerification


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['phone', 'name', 'verified', 'token', 'id']

    search_fields = ('name', 'phone', )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'verified')
    ordering = ('id', 'phone', )

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_("Personal info"), {"fields": ("name", "verified", "token", "services")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone", "password1", "password2"),
            },
        ),
    )


@admin.register(UserVerification)
class UserVerificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created', 'sent_via']
    list_filter = ['created']
    search_fields = ['user__phone']