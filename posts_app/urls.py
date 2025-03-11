from django.urls import path
from .views import PostListCreateView, PostDetailView, LikePostView
from .views import CommentCreateView, CommentListView

from .views import TimelineView


urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="posts-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:post_id>/like/", LikePostView.as_view(), name="like-post"),
    
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('timeline/', TimelineView.as_view(), name='timeline'),

]
