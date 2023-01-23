from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


class AuthorOrReadOnlyMixin():
    """Миксин для разрешение операций PUT, PATHCH, DELETE только автору
    контента"""

    def perform_update(self, serializer):
        if serializer.instance.author.id != self.request.user.id:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
