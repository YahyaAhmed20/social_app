from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, Follow
from .serializers import UserSerializer, FollowSerializer
from django.shortcuts import get_object_or_404

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user_to_follow = get_object_or_404(CustomUser, username=username)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)

        follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        if created:
            return Response({"message": "Followed successfully"}, status=201)
        else:
            return Response({"message": "Already following"}, status=400)

    def delete(self, request, username):
        user_to_unfollow = get_object_or_404(CustomUser, username=username)
        follow = Follow.objects.filter(follower=request.user, following=user_to_unfollow)
        if follow.exists():
            follow.delete()
            return Response({"message": "Unfollowed successfully"}, status=200)
        return Response({"error": "Not following this user"}, status=400)
