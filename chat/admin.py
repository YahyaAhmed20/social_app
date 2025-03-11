from django.contrib import admin

# Register your models here.
from .models import Message,UserProfile

admin.site.register(Message)
admin.site.register(UserProfile)
