from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, PostSerializer, GroupSerializer, \
    CommentSerializer

from posts.models import Post, Group, Comment, User
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет создания, редактирования, удаления, просмотра кверисета постов
    или отдельного поста"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """функция добавления текущего пользователя,
        как автора поста при создании"""
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет просмотра кверисета зарегистрированных пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет просмотра кверисета созданных в проекте групп"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет создания, редактирования, удаления, просмотра кверисета
    комментариев или отдельного комментария, принадлежащего определенному
    посту"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get("post_id"))

    def get_queryset(self):
        """Функция определения конкретного поста, к которому
        принадлежат комментарии/должен быть создан комментарий"""
        new_queryset = Comment.objects.filter(post=self.get_post())
        return new_queryset

    def perform_create(self, serializer):
        """функция добавления текущего пользователя, как автора
        комментария конкретного поста при создании нового комментария"""
        serializer.save(author=self.request.user, post=self.get_post())
