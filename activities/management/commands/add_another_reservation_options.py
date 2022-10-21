from django.core.management import BaseCommand

from activities.models import Activity


class Command(BaseCommand):
    def handle(self, *args, **options):
        squashes = Activity.objects.filter(activity_type__name__icontains="KORT 2 - Rezerwacja Squash")
        for squash in squashes:
            related = Activity.objects.get(activity_type__name__icontains="KORT 1 - Rezerwacja Squash",
                                                      hour=squash.hour, weekday=squash.weekday)
            squash.another_activity_options.add(related)