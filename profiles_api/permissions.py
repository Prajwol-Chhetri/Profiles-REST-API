from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is tring to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            # allowing user to see others profile
            return True

        # Else if the user requested method is not in SAFE_METHODS
        # return True when the user trying to change is the owner of object
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to edit only their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is tring to edit their own status"""
        if request.method in permissions.SAFE_METHODS:
            # allowing user to see others status
            return True

        # Else if the user requested method is not in SAFE_METHODS
        # return True when the user trying to change is the owner of object
        return obj.user_profile.id == request.user.id