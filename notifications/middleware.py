from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken
from channels.exceptions import DenyConnection
@database_sync_to_async
def get_user(token):
    try:
        token_obj = AccessToken(token)
        token_obj.verify()
    except:
        return None
    # token_obj.verify()
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
    user_uuid  = token_backend.decode(token)['user_uuid']
    model = get_user_model()
    try:
        return model.objects.get(uuid=user_uuid)
    except model.DoesNotExist:
        raise None


class WebsocketJWTAuthenticationMiddleware:
    def __init__(self,app):
        self.app = app

    async def __call__(self,scope,recieve,send):
        headers_dict = dict(scope['headers'])
        cookies_str = headers_dict.get(b"cookie",b"").decode()
        cookies = {cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookies_str.split("; ")}
        access_token = cookies.get("access_token")
        
        scope["token"] = access_token
        scope["user"] = await get_user(access_token)


        return await self.app(scope,recieve,send)
    