from django.contrib import admin

# Register your models here.
from .models import MessageReaction,Message

admin.site.register(MessageReaction)
admin.site.register(Message)