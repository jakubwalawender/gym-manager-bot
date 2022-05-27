import requests
from django.conf import settings
from django.core.management import BaseCommand

from reservations.models import Location


class Command(BaseCommand):
    help = 'Fetch all locations'

    def handle(self, *args, **options):
        fetch_activities()
        print(f"Done!")


def fetch_activities():
    response = requests.get(settings.LOCATIONS_URL)
    locations = response.json()
    for location in locations:
        data = {"name": location["Name"], "address": location["Address"], "city": location["City"],
                "external_id": location["Id"]}
        try:
            Location.objects.create(**data)
        except Exception as e:
            pass
