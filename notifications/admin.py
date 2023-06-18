from django.contrib import admin
from .models import (
    Notification,
    NotificationChannel
    )

admin.site.register(NotificationChannel)
admin.site.register(Notification)
