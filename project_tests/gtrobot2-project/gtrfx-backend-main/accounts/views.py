from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from accounts.models import User, UserVerification
from accounts.sendotp import send_message, send_message_via_whatsapp
from accounts.serializers import UserSerializer

import random
import string
from datetime import datetime, timedelta
import pytz


def generate_token():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(20))



class RegistrationView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        name = request.data.get('name')
        phone = request.data.get('phone')

        if not name or not phone:
            return Response({'error': 'Имя, телефон или пароль не указаны'}, status=400)

        phone = phone.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("_", "")

        if User.objects.filter(phone=phone).exists():
            return Response({'error': 'Телефон уже зарегистрирован'}, status=400)
        

        user = User.objects.create_user(name=name, phone=phone)
        code = random.randint(102021, 993721)
        user.token = generate_token()
        user.token_is_used = False
        user.save()
        code_sent_via = 'sms'
        if user.phone.startswith('+998') or user.phone.startswith('998'):
            send_message(user.phone, code)
        else:
            send_message_via_whatsapp(user.phone, code)
            code_sent_via = 'whatsapp'
        UserVerification.objects.create(user=user, code=code, sent_via=code_sent_via)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'phone': phone, 
            'verified': user.verified, 
            'user_id': user.id,
            'name': user.name,
            'user_phone': user.phone,
            'code_sent_via': code_sent_via,
            'access_token': token.key
        })
    

class VerifyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')
        if not phone or not code:
            return Response({'error': 'Телефон или код не указан'}, status=400)
        phone = phone.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("_", "")
        user = User.objects.get(phone=phone)
        if user.verified:
            return Response({'error': 'Пользователь уже подтвержден'}, status=400)
        try:
            UserVerification.objects.get(user=user, code=code)
        except UserVerification.DoesNotExist:
            return Response({'error': 'Неверный код или телефон'}, status=400)
        user.verified = True
        user.save()
        return Response({'phone': phone, 'verified': user.verified, 'user_id': user.id, 'name': user.name})
    

class ResendCodeView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        phone = request.data.get('phone')
        if not phone:
            return Response({'error': 'Телефон не указан'}, status=400)
        phone = phone.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("_", "")
        if not User.objects.filter(phone=phone).exists():
            return Response({'error': 'Такого пользователя не существует'}, status=400)
        user = User.objects.get(phone=phone)
        if user.verified:
            return Response({'error': 'Пользователь уже подтвержден'}, status=400)
        code = random.randint(102021, 993721)
        codes = UserVerification.objects.filter(user=user)
        if codes.exists():
            if codes.first().created.replace(tzinfo=pytz.utc) > datetime.now(tz=pytz.utc) - timedelta(minutes=2):
                return Response({'error': 'Код можно запросить раз в 2 минуты'}, status=400)
            codes.delete()
        code_sent_via = 'sms'
        if user.phone.startswith('+998') or user.phone.startswith('998'):
            send_message(user.phone, code)
        else:
            send_message_via_whatsapp(user.phone, code)
            code_sent_via = 'whatsapp'
        UserVerification.objects.create(user=user, code=code, sent_via=code_sent_via)
        return Response({'phone': phone, 'code_sent_via': code_sent_via})


class SendCodeView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        if not phone:
            return Response({'error': 'Телефон не указан'}, status=400)
        phone = phone.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("_", "")
        if not User.objects.filter(phone=phone).exists():
            return Response({'error': 'Такого пользователя не существует'}, status=400)
        user = User.objects.get(phone=phone)
        code = random.randint(102021, 993721)
        codes = UserVerification.objects.filter(user=user)
        if codes.exists():
            if codes.first().created.replace(tzinfo=pytz.utc) > datetime.now(tz=pytz.utc) - timedelta(minutes=2):
                return Response({'error': 'Код можно запросить раз в 2 минуты'}, status=400)
            codes.delete()
        code_sent_via = 'sms'
        if user.phone.startswith('+998') or user.phone.startswith('998'):
            send_message(user.phone, code)
            pass
        else:
            send_message_via_whatsapp(user.phone, code)
            code_sent_via = 'whatsapp'
        UserVerification.objects.create(user=user, code=code, sent_via=code_sent_via)
        return Response({'phone': phone, 'code_sent_via': code_sent_via})



class LoginView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')
        if not phone or not code:
            return Response({'error': 'Телефон или код не указан'}, status=400)
        phone = phone.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace("_", "")
        try:
            UserVerification.objects.get(user__phone=phone, code=code)
        except UserVerification.DoesNotExist:
            return Response({'error': 'Неверный код'}, status=400)
        
        user = User.objects.filter(phone=phone).first()
        if user is None:
            return Response({'error': 'Неверный код или телефон'}, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response(serializer.data | {'access_token': token.key})
    

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request.auth.delete()
        return Response({'success': True})    
    

class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)    

class UserViaTokenView(APIView):
    def post(self, request):
        token = request.data.get('token')
        if not token:
            return Response({'error': 'Токен не указан'}, status=400)
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            return Response({'error': 'Неверный токен'}, status=400)
        
        serializer = UserSerializer(user)
        paid_click = None
        paid_yookassa = None
        for order in user.click_order.all():
            paid_click = False
            if order.status == 'confirmed':
                paid_click = True
                break

        for order in user.yookassa_order.all():
            paid_yookassa = False
            if order.status == 'succeeded':
                paid_yookassa = True
                break
        data = serializer.data
        data['paid'] = paid_click is True or paid_yookassa is True

        return Response(data)