from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Право доступа пользователя, который является владельцем (создателем) сущности"""
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
