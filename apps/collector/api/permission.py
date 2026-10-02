from rest_framework.permissions import BasePermission
from apps.accounts.models import User
from apps.accounts.models import Role

class IsCollector(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == Role.COLLECTOR:
            return True
        return False
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == Role.ADMIN:
            return True
        return False