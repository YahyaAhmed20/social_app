from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message, MessageReaction
from .serializers import MessageReactionSerializer
from django.shortcuts import get_object_or_404

class MessageReactionView(APIView):
    def post(self, request, message_id):
        """إضافة أو تحديث تفاعل على رسالة"""
        message = get_object_or_404(Message, id=message_id)
        user = request.user
        emoji = request.data.get("emoji")

        if not emoji:
            return Response({"error": "Emoji is required"}, status=status.HTTP_400_BAD_REQUEST)

        reaction, created = MessageReaction.objects.update_or_create(
            message=message,
            user=user,
            defaults={"emoji": emoji}
        )

        serializer = MessageReactionSerializer(reaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    def delete(self, request, message_id):
        """إزالة التفاعل"""
        message = get_object_or_404(Message, id=message_id)
        user = request.user
        reaction = MessageReaction.objects.filter(message=message, user=user)

        if reaction.exists():
            reaction.delete()
            return Response({"message": "Reaction removed"}, status=status.HTTP_204_NO_CONTENT)

        return Response({"error": "Reaction not found"}, status=status.HTTP_404_NOT_FOUND)
