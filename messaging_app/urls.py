from django.urls import path
from .views import MessageReactionView

urlpatterns = [
    path('messages/<int:message_id>/reactions/', MessageReactionView.as_view(), name='message-reactions'),
]
