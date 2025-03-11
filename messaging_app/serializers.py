from rest_framework import serializers
from .models import MessageReaction

class MessageReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageReaction
        fields = "__all__"
    