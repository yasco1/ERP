from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save,sender=Notification)
def NotificationWebsockerTrigger(sender,instance,created,*args,**kwargs):
    print(instance)
    # if created:
    #     async_to_sync(channel_layer.group_send)(
    #         "Broadcast",
    #         {
    #             'type':'notification.message',
    #             'title':instance.title,
    #             'body':instance.body
    #         },
    #     )