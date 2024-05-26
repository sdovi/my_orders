from django.urls import path
from payments.views import YookassaOrderView, YookassaCheckView, CreateClickTransactionView, ClickTransactionView

urlpatterns = [
    path('yookassa/create/', YookassaOrderView.as_view(), name='yookassa-create'),
    path('yookassa/check/', YookassaCheckView.as_view(), name='yookassa-check'),
    path('yookassa/webhook/', ClickTransactionView.as_view(), name='yookassa-webhook'),
    path('click/create/', CreateClickTransactionView.as_view(), name='click-create'),
    path('click/done/', ClickTransactionView.as_view(), name='click-done'),
]
