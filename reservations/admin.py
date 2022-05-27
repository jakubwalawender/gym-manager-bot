from django.contrib import admin
from django.contrib.auth.models import Group

from reservations.models import PossibleReservation, Location, ReservationType


@admin.register(ReservationType)
class ReservationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(PossibleReservation)
class PossibleReservationAdmin(admin.ModelAdmin):
    list_display = ('type', 'weekday', 'hour', 'activity_id')
    search_fields = ('type__name', 'weekday', 'hour', 'activity_id')
    filter_horizontal = ('another_reservation_options',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'external_id')
    search_fields = ('name', 'address', 'city', 'external_id')


admin.site.unregister(Group)
