from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """Проверка прав доступа для владельцев."""

    def has_object_permission(self, request, view, obj):
        """Проверяет, является ли пользователь владельцем."""
        return obj.user == request.user
