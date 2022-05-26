from django.contrib import admin

from reservations.models import ReservationType, PossibleReservation

@admin.register(PossibleReservation)
class PossibleReservationAdmin(admin.ModelAdmin):
    list_display = ('type', 'weekday', 'hour', 'activity_id')
    search_fields = ('type__name', 'weekday', 'hour', 'activity_id')
    filter_horizontal = ('another_reservation_options',)