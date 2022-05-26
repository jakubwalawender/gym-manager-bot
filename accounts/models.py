from django.contrib.auth.models import AbstractUser
from django.db import models

from reservations.models import PossibleReservation


class User(AbstractUser):
    gym_manager_login = models.CharField(max_length=200, unique=True, blank=True, null=True)
    gym_manager_password = models.CharField(max_length=200, blank=True, null=True)
    gym_manager_id = models.IntegerField(unique=True, blank=True, null=True)
    reservations = models.ManyToManyField(PossibleReservation, blank=True)
