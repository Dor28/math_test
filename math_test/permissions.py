from rest_framework import permissions


class StudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not hasattr(request.user, 'student'):
            return self.handle_no_permission()
        return super().has_permission(request, view)


class TeacherPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not hasattr(request.user, 'teacher'):
            return self.handle_no_permission()
        return super().has_permission(request, view)


