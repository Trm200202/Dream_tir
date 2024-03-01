from rest_framework import permissions


class ProfilePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return user.auth_status == 'code_verified'
