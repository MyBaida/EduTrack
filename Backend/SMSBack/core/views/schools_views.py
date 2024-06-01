from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser 

from core.models import Class, School
from core.serializers import SchoolSerializer, CreateUserSerializer
from core.permissions import IsSuperAdmin, IsSchoolAdmin, IsTeacher, IsTeacherOfSubject, IsSchoolAdminOfSchool


from rest_framework import status

@api_view(['POST'])
@permission_classes([IsSuperAdmin])
def create_school_with_admin(request):
    user_data = {
        'username': request.data.get('username'),
        'password': request.data.get('password'),
        'email': request.data.get('email'),
        # 'first_name': request.data.get('first_name'),
        # 'last_name': request.data.get('last_name'),
        'role': 'school_admin'
    }

    user_serializer = CreateUserSerializer(data=user_data)
    if user_serializer.is_valid():
        school_admin = user_serializer.save()

        school_data = {
            'name': request.data.get('name'),
            'school_type': request.data.get('school_type'),
            'address': request.data.get('address'),
            'phone': request.data.get('phone'),
            'admin': school_admin.id
        }

        school_serializer = SchoolSerializer(data=school_data)
        if school_serializer.is_valid():
            school_serializer.save()
            return Response({
                'school': school_serializer.data,
                'school_admin': user_serializer.data
            }, status=status.HTTP_201_CREATED)

        school_admin.delete()  
        return Response(school_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
