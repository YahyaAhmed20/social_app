from rest_framework import serializers
from .models import CustomUser, Follow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "username", "profile_picture", "bio"]

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["follower", "following", "created_at"]
