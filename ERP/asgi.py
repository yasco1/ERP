import os

from channels.security.websocket import AllowedHostsOriginValidator

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ERP.settings")

django_application = get_asgi_application()

from . import urls  # noqa isort:skip
from notifications.middleware import WebsocketJWTAuthenticationMiddleware # noqa isort:skip

application = ProtocolTypeRouter(
    { "http": get_asgi_application(),
      "websocket": AllowedHostsOriginValidator(
          WebsocketJWTAuthenticationMiddleware(
          URLRouter(urls.websocket_urlpatterns)
          )
          )
      }
)
