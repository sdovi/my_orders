from payments.models import YookassaOrder
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from yookassa import Configuration, Payment as YookassaPayment, Webhook
from yookassa.domain.notification import WebhookNotification

import uuid
import json

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

from django.conf import settings

from pyclick.utils import PyClickMerchantAPIView
from pyclick.serializers import ClickTransactionSerializer
from pyclick.views import TransactionCheck

from payments.models import ClickOrder

from accounts.models import User

Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

# webhook_list = Webhook.list()
# webhook_is_set = False
# for webhook in webhook_list.items:
#     if webhook.url == settings.YOOKASSA_WEBHOOK_URL:
#         webhook_is_set = True
#         break


# if not webhook_is_set:
#     Webhook.add({
#         "event": "payment.waiting_for_capture",
#         "url": settings.YOOKASSA_WEBHOOK_URL,
#     })


class YookassaOrderView(APIView):
    permission_classes = [IsAuthenticated]

    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def post(self, request):
        amount = request.data.get('amount')
        if not amount:
            return HttpResponseBadRequest('Amount is required')
        amount = float(amount) * 93
        order = YookassaOrder.objects.create(amount=float(amount), user=request.user)
        try:
            params = {
                "amount": {
                    "value": order.amount,
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": settings.SERVER_URL
                },
                "capture": True,
                "description": "GTRobot payment for order No. " + str(order.id),
                "metadata": {
                    "order_id": order.id
                },
                "receipt": {
                    "customer": {
                        "email": "GTRobot@mail.ru"
                    },
                    "items": [
                        {
                            "description": "Услуга 1",
                            "quantity": "1.00",
                            "amount": {
                                "value": str(order.amount),
                                "currency": "RUB"
                            },
                            "vat_code": "4",
                            "payment_mode": "full_prepayment",
                            "payment_subject": "marked",
                            "measure": "piece"
                        }
                    ]
                }
            }
            response = YookassaPayment.create(params)
        except Exception as e:
            return HttpResponseBadRequest(e)

        order.yookassa_id = response.id
        order.status = response.status
        order.yookassa_created_at = response.created_at
        order.paid = response.paid
        order.recipient_account_id = response.recipient.account_id
        order.recipient_gateway_id = response.recipient.gateway_id
        order.save()

        return JsonResponse(
            {
                'redirect_url': response.confirmation.confirmation_url,
                'id': order.yookassa_id
            }
        )
    

class YookassaWebhookView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        webhook_object = WebhookNotification(data)
        payment = webhook_object.object
        order = get_object_or_404(YookassaOrder, yookassa_id=payment.id)
        payment = YookassaPayment.capture(order.yookassa_id)
        order.yookassa_id = payment.id
        order.status = payment.status
        order.yookassa_created_at = payment.created_at
        order.paid = payment.paid
        order.recipient_account_id = payment.recipient.account_id
        order.recipient_gateway_id = payment.recipient.gateway_id

        order.save()

        if order.status == 'succeeded':
            order.user.subscription_start = timezone.now()
            order.user.subscription_end = timezone.now() + timedelta(days=order.user.subscription_day)
            order.user.save()

        return JsonResponse({'status': 'ok'})


class YookassaCheckView(APIView):
    permission_classes = [IsAuthenticated]

    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        order_id = request.query_params.get('order_id')
        if not order_id:
            return HttpResponseBadRequest('Order ID is required')
        order = YookassaOrder.objects.get(id=order_id)
        try:
            response = YookassaPayment.find_one(order.yookassa_id)
        except Exception as e:
            return HttpResponseBadRequest(e)
        
        if response.status == 'waiting_for_capture':
            response = YookassaPayment.capture(order.yookassa_id, idempotence_key=str(uuid.uuid4()))
        order.yookassa_id = response.id
        order.status = response.status
        order.yookassa_created_at = response.created_at
        order.paid = response.paid
        order.recipient_account_id = response.recipient.account_id
        order.recipient_gateway_id = response.recipient.gateway_id
        order.save()
        if order.status == 'succeeded':
            order.user.subscription_start = timezone.now()
            order.user.subscription_end = timezone.now() + timedelta(days=order.user.subscription_day)
            order.user.save()
        return JsonResponse(
            {
                'status': order.status,
                'id': order.yookassa_id,
                'created_at': order.yookassa_created_at,
                'paid': order.paid
            }
        )
        
    



class CreateClickTransactionView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    serializer_class = ClickTransactionSerializer

    def post(self, request, *args, **kwargs):
        amount = request.POST.get('amount')
        if not amount:
            return JsonResponse({'error': 'Amount is required'})
        amount = float(amount) * 12600
        order = ClickOrder.objects.create(amount=amount, user=request.user)
        return_url = settings.SERVER_URL
        url = PyClickMerchantAPIView.generate_url(order_id=order.id, amount=str(amount), return_url=return_url)
        return JsonResponse({
            'redirect_url': url,
            'id': order.id
        })
    

class ClickTransactionCheck(TransactionCheck):
    @classmethod
    def successfully_payment(cls, transaction):
        transaction.user.subscription_start = timezone.now()
        transaction.user.subscription_end = transaction.user.subscription_start + timedelta(days=transaction.user.subscription_day)
        transaction.user.save()

class ClickTransactionView(PyClickMerchantAPIView):
    VALIDATE_CLASS = ClickTransactionCheck
    @classmethod
    def order_load(cls, order_id):
        if int(order_id) > 1000000000:
            return None
        transaction = get_object_or_404(ClickOrder, id=int(order_id))
        return transaction