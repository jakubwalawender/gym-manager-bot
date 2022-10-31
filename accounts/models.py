from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from encrypted_model_fields.fields import EncryptedCharField

from activities.models import Activity

"""
Custom user model with gym_manager credentials, and activities
"""


class User(AbstractUser):
    gym_manager_login = EncryptedCharField(
        max_length=200, blank=True, null=True)
    gym_manager_password = EncryptedCharField(
        max_length=200, blank=True, null=True)
    gym_manager_id = models.IntegerField(unique=True, blank=True, null=True)
    activities = models.ManyToManyField(
        Activity, blank=True, through='UserActivity')


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    requires_confirmation = models.BooleanField(default=True)
    minutes_to_auto_cancel = models.IntegerField(default=180, validators=[
        MinValueValidator(121),
    ],)

    class Meta:
        verbose_name_plural = "user activities"
