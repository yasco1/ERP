from django.db import models
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist

class NotificationChannelManager(models.Manager):
        
    def create_user_notification_channel(self,user):
        channel = {
            "channel_name":user.uuid
        }
        user_notification_channel = NotificationChannel.objects.create(**channel)
        user_notification_channel.save()
        return user_notification_channel


class NotificationChannel(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    channel_name = models.CharField(max_length=100)

    objects=NotificationChannelManager()

    def __str__(self) -> str:
        return f"{self.channel_name}"

class Notification(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    notification_channel = models.ForeignKey(NotificationChannel,on_delete=models.CASCADE,related_name="Notifications",null=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    read_user = models.ManyToManyField(get_user_model() ,related_name="ReadNotifications")
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save,sender=Notification)
def NotificationWebsockerTrigger(sender,instance,created,*args,**kwargs):
    channel_layer = get_channel_layer()
    if created:
        if instance.notification_channel:
            async_to_sync(channel_layer.group_send)(
                    instance.notification_channel.channel_name,
                    {
                        'type':'notification.message',
                        'title':instance.title,
                        'body':instance.body
                    },
                )
        elif instance.user:
            pass