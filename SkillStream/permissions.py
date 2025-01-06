from rest_framework import permissions

class IsInstructorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow instructors to create or modify courses.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write access only if the user is an instructor
        return request.user.profile.is_instructor