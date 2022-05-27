import json
from datetime import datetime
import calendar
import requests as requests
from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError

from reservations.models import PossibleReservation, ReservationType, Location

from reservations.management.get_token import get_token


class Command(BaseCommand):
    help = 'Hit classes endpoint and get all (id, day, hour) combinations for an activity which name equals provided string'

    def handle(self, *args, **options):
        fetch_activities()
        print(f"Done!")


def fetch_activities():
    locations = Location.objects.all()
    for location in locations:
        CLASSES_BODY = {
            "Days": 7,
            "LocationId": location.external_id,
            "StartDate": datetime.today().strftime("%a, %d %b %Y 00:00:00 GMT")
        }
        response = requests.post(settings.CLASSES_URL, json=CLASSES_BODY)
        data = response.json()
        all_reservation_type_names = set([x["Name"] for x in data])
        for reservation_type_name in all_reservation_type_names:
            try:
                ReservationType.objects.create(name=reservation_type_name)
            except IntegrityError as e:
                continue
        for activity in data:
            type = ReservationType.objects.get(name=activity["Name"])
            date = datetime.strptime(activity["StartTime"], '%Y-%m-%dT%H:%M:%SZ')
            weekday = calendar.day_name[date.weekday()]
            hour = f"{datetime.strftime(date, '%H')}:{datetime.strftime(date, '%M')}"
            id = activity["Id"]
            try:
                PossibleReservation.objects.create(
                    **{"weekday": weekday_string_to_choice(weekday), "hour": hour, "activity_id": id, "type": type,
                       "location": location})
            except IntegrityError as e:
                continue


def weekday_string_to_choice(weekday):
    days_dict = {
        "Monday": PossibleReservation.Weekday.MONDAY,
        "Tuesday": PossibleReservation.Weekday.TUESDAY,
        "Wednesday": PossibleReservation.Weekday.WEDNESDAY,
        "Thursday": PossibleReservation.Weekday.THURSDAY,
        "Friday": PossibleReservation.Weekday.FRIDAY,
        "Saturday": PossibleReservation.Weekday.SATURDAY,
        "Sunday": PossibleReservation.Weekday.SUNDAY,
    }
    return days_dict[weekday]
