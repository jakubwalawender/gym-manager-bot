from django.contrib import admin
from django.contrib.auth.models import Group

from activities.models import Activity, Location, ActivityType


@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'weekday', 'hour', 'activity_id')
    search_fields = ('activity_type__name', 'weekday', 'hour', 'activity_id')
    filter_horizontal = ('another_activity_options',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'external_id')
    search_fields = ('name', 'address', 'city', 'external_id')


admin.site.unregister(Group)
