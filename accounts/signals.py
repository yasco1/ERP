from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from websocketcore.models import WebsocketChannel

@receiver(post_save,sender=get_user_model())
def migrations_with_Websocket_channels(sender,instance,created,*args,**kwargs):
    print('Start Create Websocket Channels')
    if created:
        print('Start Create Websocket Channels')
        WebsocketChannel.objects.create_for_user(instance)