from rest_framework import permissions
from .models import *

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'super_admin'

class IsSchoolAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(f"User role: {request.user.role}")
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
            try:
                school = School.objects.get(admin=request.user)
                print(request.user)
                print(school.admin)
                request.school = school  # Store the school in the request for later use
                return True
            except School.DoesNotExist:
                return False
        return False

# class IsSchoolAdminOfSchool(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user and request.user.role == 'school_admin':
#             user_school = School.objects.filter(admin=request.user).first()
#             print(request.user)
#             print(user_school.admin)
#             if user_school and 'school_id' in request.data and request.data['school_id'] == user_school._id:
#                 request.school = user_school  # Store the school in the request for later use
#                 return True
#         return False