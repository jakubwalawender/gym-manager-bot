from django.core.management import BaseCommand

from reservations.models import PossibleReservation

class Command(BaseCommand):
    def handle(self, *args, **options):
        squashes = PossibleReservation.objects.filter(type__name__icontains="KORT 2 - Rezerwacja Squash")
        for squash in squashes:
            related = PossibleReservation.objects.get(type__name__icontains="KORT 1 - Rezerwacja Squash",
                                                      hour=squash.hour, weekday=squash.weekday)
            squash.another_reservation_options.add(related)