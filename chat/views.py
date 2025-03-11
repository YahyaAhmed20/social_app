from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from datetime import timedelta
from .models import Message


User = get_user_model()

def get_last_seen(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        profile = UserProfile.objects.get(user=user)
        return JsonResponse({"last_seen": profile.last_seen})
    except UserProfile.DoesNotExist:
        return JsonResponse({"error": "User profile not found"}, status=404)


def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    if message.sender != request.user:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    if now() - message.timestamp > timedelta(minutes=5):
        return JsonResponse({"error": "Message can no longer be deleted"}, status=400)

    message.deleted = True
    message.save()
    return JsonResponse({"success": "Message deleted"})