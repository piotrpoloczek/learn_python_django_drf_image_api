from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view and edit.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author.id == request.user.id