from django.views.generic import RedirectView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Service, StoreModel
from .serializers import ServiceSerializer

class IndexView(RedirectView):
    url = 'https://gtrobot.shop/'


class ServicesView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



class UserBuyService(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        services = request.data.get('services')
        days = request.data.get('days')
        user = request.user
        user.subscription_day = days or 0
        for service_id in services:
            service = Service.objects.get(id=service_id)
            user.services.add(service)
        return Response({'status': 'ok'})
