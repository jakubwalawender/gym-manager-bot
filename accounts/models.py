from django.contrib.auth.models import AbstractUser
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

from reservations.models import PossibleReservation


class User(AbstractUser):
    gym_manager_login = EncryptedCharField(max_length=100, blank=True, null=True)
    gym_manager_password = EncryptedCharField(max_length=100, blank=True, null=True)
    gym_manager_id = models.IntegerField(unique=True, blank=True, null=True)
    reservations = models.ManyToManyField(PossibleReservation, blank=True)
