from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, UserViewSet, GroupViewSet, CommentViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('users', UserViewSet, basename='user')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)


urlpatterns = [
    path('', include(v1_router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
