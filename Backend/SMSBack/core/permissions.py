from rest_framework import permissions
from .models import *

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'super_admin'

class IsSchoolAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'school_admin'

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'teacher'

class IsTeacherOfSubject(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.role == 'teacher':
            teacher = Teacher.objects.get(user=request.user)
            subject_id = view.kwargs.get('subject_id')
            # Check if the teacher is assigned to the subject
            return teacher.subjects.filter(id=subject_id).exists()
        return False

class IsSchoolAdminOfSchool(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.role == 'school_admin':
            # Get the school ID from the request URL or query parameters
            school_id = request.query_params.get('school_id') or view.kwargs.get('school_id')
            # Check if the school admin belongs to the school
            return School.objects.filter(id=school_id, admin=request.user).exists()
        return False

