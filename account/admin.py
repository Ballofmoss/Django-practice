from django.contrib import admin
from account.models import Profile
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass
