import calendar
import requests as requests
from datetime import datetime
from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError

from activities.management.weekday_string_to_choice import weekday_string_to_choice
from activities.models import Activity, Activity, ActivityType, Location


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
        all_activity_type_names = set([x["Name"] for x in data])
        for activity_type_name in all_activity_type_names:
            try:
                ActivityType.objects.create(name=activity_type_name)
            except IntegrityError as e:
                continue
        for activity in data:
            activity_type = ActivityType.objects.get(name=activity["Name"])
            date = datetime.strptime(activity["StartTime"], '%Y-%m-%dT%H:%M:%SZ')
            weekday = calendar.day_name[date.weekday()]
            hour = f"{datetime.strftime(date, '%H')}:{datetime.strftime(date, '%M')}"
            id = activity["Id"]
            try:
                Activity.objects.create(
                    **{"weekday": weekday_string_to_choice(weekday), "hour": hour, "activity_id": id, "activity_type": activity_type,
                       "location": location})
            except IntegrityError as e:
                continue

