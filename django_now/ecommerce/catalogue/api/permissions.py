from rest_framework import permissions


class HasAdminPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
    	if request.user.is_staff or request.user.is_superuser:
    		return True