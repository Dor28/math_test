from rest_framework import permissions


class StudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return not hasattr(request.user, 'student')
       


class TeacherPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return not hasattr(request.user, 'teacher')



      


