from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

from personnel.models import Employment_Info
from uuid import uuid4
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken,
    BlacklistedToken,
)
# from notifications.models import NotificationChannel


class AccountManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        # user_notification_channel = NotificationChannel.objects.create()
        # broadcast_notification_channel = NotificationChannel.objects.add_to_broadcast_channel(user)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email), username=username, password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_HR = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    employee = models.OneToOneField(
        Employment_Info, on_delete=models.CASCADE, related_name="account", null=True
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_HR = models.BooleanField(default=False)
    is_PR = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        if self.employee:
            return self.employee.personal_info.name_ar
        else:
            return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
