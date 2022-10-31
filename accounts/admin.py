from django.contrib import admin
from accounts.models import User, UserActivity
from activities.models import Activity



class UserActivitiesInline(admin.TabularInline):
    model = UserActivity
    extra = 1
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)
    inlines = (UserActivitiesInline,)