from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username')
    search_fields = ('username')
    filter_horizontal = ('reservations',)
    # exclude = ('gym_manager_login', 'gym_manager_password', 'gym_manager_id')