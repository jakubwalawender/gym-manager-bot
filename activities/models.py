from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class ActivityType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    external_id = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    class Weekday(models.TextChoices):
        MONDAY = "MO", _("Monday")
        TUESDAY = "TU", _("Tuesday")
        WEDNESDAY = "WE", _("Wednesday")
        THURSDAY = "TH", _("Thursday")
        FRIDAY = "FR", _("Friday")
        SATURDAY = "SA", _("Saturday")
        SUNDAY = "SU", _("Sunday")

    hour = models.CharField(max_length=5, validators=[RegexValidator("^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")])
    weekday = models.CharField(max_length=2, choices=Weekday.choices, default=Weekday.MONDAY)
    activity_type = models.ForeignKey("ActivityType", on_delete=models.CASCADE)
    activity_id = models.IntegerField()
    another_activity_options = models.ManyToManyField("self", blank=True, symmetrical=False, through='ActivityActivity')
    location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ("hour", "weekday", "activity_type", "activity_id")

    def __str__(self):
        return f"{self.location.name} - {self.activity_type.name} - {self.get_weekday_display()} - {self.hour}"


class ActivityActivity(models.Model):
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)