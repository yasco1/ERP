from .models import NotificationChannel,Notification


# class Notification(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True, default=uuid4, unique=True, editable=False
#     )
#     notification_channel = models.ForeignKey(NotificationChannel,on_delete=models.CASCADE,related_name="Notifications",null=True)
#     user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
#     title = models.CharField(max_length=100)
#     body = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)

class BroadCastNotificationMixin:
    
    @staticmethod
    def _get_broadcast_channel():
        try:
            return NotificationChannel.objects.get(channel_name="Broadcast")
        except NotificationChannel.DoesNotExist:
            None
    
    def _create_notification(self,response):
        notification_channel = self._get_broadcast_channel()
        notification = {
            "notification_channel": notification_channel,
            "title":"notification_title",
            "body":"notification_body"
        }
        Notification.objects.create(**notification)

    def finalize_response(self,request,response,*args,**kwargs):
        response = super().finalize_response(request,response,*args,**kwargs)
        self._create_notification(response)
        return response

class IndividualNotificationMixin:
    def finalize_response(self,request,response,*args,**kwargs):
        
        return super().finalize_response(request,response,*args,**kwargs)