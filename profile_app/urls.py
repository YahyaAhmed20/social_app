from django.urls import path
from .views import UserProfileView, FollowUserView

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("follow/<str:username>/", FollowUserView.as_view(), name="follow-user"),
]
