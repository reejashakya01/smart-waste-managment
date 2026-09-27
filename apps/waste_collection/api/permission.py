
from rest_framework.permissions import BasePermission
from apps.accounts.models import Role

class IsCustomerOrAdmin(BasePermission):
    """
    Allows access only to customer and admin  users.
    """
    help_text = "Permission Denied for Collector"

    def has_permission(self, request, view):
        # return bool(request.user and request.user.is_authenticated)
        if request.user.role == Role.CUSTOMER:
            return True
        else:
            return False