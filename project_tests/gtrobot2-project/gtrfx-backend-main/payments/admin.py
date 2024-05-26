from django.contrib import admin
from payments.models import YookassaOrder, ClickOrder
from pyclick.admin import ClickTransactionAdmin


@admin.register(YookassaOrder)
class YookassaOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'paid', 'yookassa_id', 'status', 'recipient_account_id',
                    'recipient_gateway_id', 'yookassa_created_at', 'created_at']
    

@admin.register(ClickOrder)
class ClickOrderAdmin(ClickTransactionAdmin):
    ist_display = ('id', 'click_paydoc_id', 'amount', 'status', 'user')
