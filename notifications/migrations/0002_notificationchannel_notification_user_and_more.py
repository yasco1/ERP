# Generated by Django 4.2.2 on 2023-06-15 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationChannel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('channel_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Notifications', to='notifications.notificationchannel'),
        ),
    ]
