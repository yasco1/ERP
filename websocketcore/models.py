from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from notifications.models import NotificationChannel

class WebsocketChannelManager(models.Manager):
    def _create_user_notification_channel(self,user):
        return NotificationChannel.objects.create_user_notification_channel(user)
    
    def _get_broadcast_notification_channel(self):
        try:
            return NotificationChannel.objects.get(channel_name = "Broadcast")
        except NotificationChannel.DoesNotExist:
            return None

    def create_for_user(self,user):
        WebsocketChannelsData = {
            "user":user,
        }
        wsc = WebsocketChannel.objects.create(**WebsocketChannelsData)
        wsc.notification_channels.add(
            self._get_broadcast_notification_channel(),
            self._create_user_notification_channel(user)
            )
        # TO ADD TASK MANAGER CHANNELS 
        # TO ADD CHAT CHANNELS
        wsc.save()
        return wsc

    def get_for_user(self,user):
        try:
            return WebsocketChannel.objects.get(user=user)
        except:
            return None

class WebsocketChannel(models.Model):
    uuid = models.UUIDField(default=uuid4,primary_key=True,unique=True,editable=False)
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name="WebsocketChannels")
    notification_channels = models.ManyToManyField(NotificationChannel,related_name="AssignedUsers")

    objects = WebsocketChannelManager()
      
