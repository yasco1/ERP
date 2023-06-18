from django.urls import path, include
from .consumers import (
    BroadcastNotificationConsumber,
)

websocket_urlpatterns = [
    path("broadcast", BroadcastNotificationConsumber.as_asgi()),
    ]