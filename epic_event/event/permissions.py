from rest_framework import permissions


SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True


class CompanyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user.has_perm("event.view_company"):
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.has_perms(["event.change_company", "event.delete_company"]):
            return True

        if (
            request.user.has_perm("event.view_company")
            and request.method in SAFE_METHODS
        ):
            return True


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user.has_perm("event.view_contract"):
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.has_perms(["event.change_contract", "event.delete_contract"]):
            return True

        if (
            request.user.has_perm("event.view_contract")
            and request.method in SAFE_METHODS
        ):
            return True


class EventPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user.has_perm("event.view_event"):
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.has_perms(["event.change_event", "event.delete_event"]):
            return True

        if request.user.has_perm("event.view_event") and request.method in SAFE_METHODS:
            return True


class CompanyEventsPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.user.has_perm("event.view_companyevents"):
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.has_perms(
            ["event.change_companyevents", "event.delete_companyevents"]
        ):
            return True

        if (
            request.user.has_perm("event.view_companyevents")
            and request.method in SAFE_METHODS
        ):
            return True
