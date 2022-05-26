from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'gym_manager_login', 'gym_manager_id')
    search_fields = ('username', 'gym_manager_login', 'gym_manager_id')
    filter_horizontal = ('reservations',)