from rest_framework.permissions import BasePermission
from .models import Mensajes

class IsOwner(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        print("Inside object permissions")
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, Mensajes):
            return obj.sender == request.user
        return obj.sender == request.user
