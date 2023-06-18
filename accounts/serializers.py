from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)
from .models import Account
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError, FieldDoesNotExist
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)
from rest_framework import status
from django.utils.translation import gettext_lazy as _

import re

class JWTTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        if user.employee:
            token["emp_uuid"] = str(user.employee.personal_info.uuid)
            token["emp_name_ar"] = str(user.employee.personal_info.name_ar)
            token["emp_name_en"] = str(user.employee.personal_info.name_en)
            token["is_hr"] = str(user.is_HR)
            token["is_pr"] = str(user.is_PR)
            return token

        raise AuthenticationFailed


class authfailedExp(AuthenticationFailed):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _("No active account found with the given credentials")
    default_code = "no_active_account"


class JWTTokenRefreshSerializer(serializers.Serializer):
    token_class = RefreshToken
    token_backend = TokenBackend(
        api_settings.ALGORITHM,
        api_settings.SIGNING_KEY,
        api_settings.VERIFYING_KEY,
        api_settings.AUDIENCE,
        api_settings.ISSUER,
        api_settings.JWK_URL,
        api_settings.LEEWAY,
        api_settings.JSON_ENCODER,
    )

    def validate(self, attrs):
        # Get Cookies From Request headers
        cookies_str = self.context['request'].META.get('HTTP_COOKIE')

        # Splite Cookies String and set cookies into Dict.
        cookies = {cookie.split("=")[0] : cookie.split("=")[1] for cookie in cookies_str.split("; ")}

        # Create Refresh Token Object For Old Refresh Token
        old_refresh = self.token_class(cookies.get('refresh_token'))

        # Check if token is expired
        old_refresh.check_exp()

        # Check if token is blacklisted
        self.get_token_from_blacklisted(cookies.get('refresh_token'))

        # Get User From Token
        user = self.get_user_from_token(cookies.get('refresh_token'))

        # Check User Authentication Rule (Activity)
        if not api_settings.USER_AUTHENTICATION_RULE(user):
            raise authfailedExp

        # Create Refresh New Refresh Token For User
        token = self.token_class.for_user(user)

        # Add Data to Token
        if user.employee:
            token["emp_uuid"] = str(user.employee.personal_info.uuid)
            token["emp_name_ar"] = str(user.employee.personal_info.name_ar)
            token["emp_name_en"] = str(user.employee.personal_info.name_en)
            token["is_hr"] = str(user.is_HR)
            token["is_pr"] = str(user.is_PR)

        # Return Data
        data = {"access": str(token.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    old_refresh.blacklist()
                except AttributeError:
                    pass

            data["refresh"] = str(token)

        return data
    
    def get_token_from_outstanding(self, token):
        try:
            jti = self.token_backend.decode(token)["jti"]
            return OutstandingToken.objects.get(jti=jti)
        except:
            raise InvalidToken

    def get_token_from_blacklisted(self, token):
        outstandingToken = self.get_token_from_outstanding(token=token)
        try:
            BlacklistedToken.objects.get(token=outstandingToken)
            raise InvalidToken
        except BlacklistedToken.DoesNotExist:
            pass

    def get_user_from_token(self, token):
        try:
            uuid = self.token_backend.decode(token)["user_uuid"]
            user = Account.objects.get(uuid=uuid)
            return user
        except:
            raise InvalidToken

# Start Account Serializers:
# # Start Account Default Serializer:


class Update_password(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ["uuid", "old_password", "new_password", "confirm_password"]

    def validate(self, data):
        # Check Old Password
        if not self.instance.check_password(data.get("old_password")):
            raise ValidationError("Old password is incorrect")

        # Check Similarity
        if not data.get("new_password") == data.get("confirm_password"):
            raise ValidationError("Passwords are not similar")

        # Validate Password
        validate_password(data.get("new_password"))

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("new_password"))
        instance.save()
        return instance

