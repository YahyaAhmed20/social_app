from django.urls import path
from .views import get_last_seen
from .views import delete_message

urlpatterns = [
    path('last-seen/<int:user_id>/', get_last_seen, name='last-seen'),
    path('delete-message/<int:message_id>/', delete_message, name='delete-message'),

]
