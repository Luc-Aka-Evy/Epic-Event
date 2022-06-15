from rest_framework import permissions


class IsAdmin(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        permission = super().has_permission
        if permission and request.user.is_superuser:
            return True


class CompanyPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        permission = super().has_permission
        if permission:
            return True

    def has_object_permission(self, request, view, obj):
        object_permission = super().has_object_permission(request, view, obj)
        if object_permission:
            return True


class ContractPermissions(permissions.DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        object_permission = super().has_object_permission(request, view, obj)
        if object_permission and obj.seller == request.user:
            return True


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        permission = super().has_permission
        if permission:
            return True

    def has_object_permission(self, request, view, obj):
        object_permission = super().has_object_permission(request, view, obj)
        if object_permission and obj.support == request.user:
            return True
