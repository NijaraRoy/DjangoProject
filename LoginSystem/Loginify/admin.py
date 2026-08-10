from django.contrib import admin
from .models import UserDetails
# Register your models here.

# admin.site.register(UserDetails)


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email")
    
admin.site.register(UserDetails, UserDetailsAdmin)