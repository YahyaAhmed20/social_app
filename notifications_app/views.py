from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from .serializers import NotificationSerializer

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def send_notification(request):
    message = request.data.get("message", "")

    notification = Notification.objects.create(user=request.user, message=message)
    serializer = NotificationSerializer(notification)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{request.user.id}",
        {"type": "send_notification", "message": message},
    )

    return Response(serializer.data, status=201)
