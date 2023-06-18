from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken
from .mixins import JWTSetCookieMixin,JWTDeleteCookieMixin
from notifications.mixins import BroadCastNotificationMixin
from django.conf import settings
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
from .serializers import (
    Update_password,
    JWTTokenRefreshSerializer,
    JWTTokenObtainSerializer
)

class JWTTokenObtainView(JWTSetCookieMixin,TokenObtainPairView):
    serializer_class = JWTTokenObtainSerializer


class JWTTokenRefreshView(JWTSetCookieMixin,BroadCastNotificationMixin,TokenRefreshView):
    serializer_class = JWTTokenRefreshSerializer

class UpdatePasswordAPIView(APIView):
    main_model_class = Account

    def get_object(self, uuid):
        try:
            return self.main_model_class.objects.get(uuid=uuid)
        except self.main_model_class.DoesNotExist:
            raise Http404
        
    def put(self, request, uuid):
        user = self.get_object(uuid=uuid)
        if request.user.uuid == user.uuid:
            serializer = Update_password(user, request.data)
            if serializer.is_valid():
                serializer.save()
                tokens = OutstandingToken.objects.filter(user=user)
                for token in tokens:
                    t, _ = BlacklistedToken.objects.get_or_create(token=token)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"error_message": "Only the same user can change his password!"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LogoutAPIView(JWTDeleteCookieMixin, APIView):
    def post(self, request):
        raw_token = request.COOKIES.get(settings.SIMPLE_JWT['REFRESH_TOKEN_NAME']) or None
        if raw_token:
            token = RefreshToken(raw_token)
            token.blacklist()
        return Response("Success", status=status.HTTP_200_OK)
