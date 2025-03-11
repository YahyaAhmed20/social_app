from django.contrib import admin

# Register your models here.

from .models import CustomUserManager, CustomUser ,Follow

admin.site.register(CustomUser)

class CustomUserManager(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # Adjust fields as needed
    search_fields = ('username', 'email')


admin.site.register(Follow)
