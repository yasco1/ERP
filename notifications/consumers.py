import json

from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

class BroadcastNotificationConsumber(JsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.NotificationGroup = "Broadcast"
        self.user = None
  
    def connect(self):
        if self.scope['user'] is None:
            self.close(4001)
        else:
            self.accept()
            async_to_sync(self.channel_layer.group_add)(
                self.NotificationGroup,
                self.channel_name,
            )

    def receive_json(self, content):
        self.close()

    def notification_message(self,event):
        self.send_json(event)

    def disconnect(self, close_code):
        pass  # Called when the socket closes