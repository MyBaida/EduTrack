from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser 

from core.models import Class, School, Teacher
from core.serializers import SchoolSerializer, CreateUserSerializer, TeacherSerializer
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


@api_view(['GET'])
@permission_classes([IsSchoolAdminOfSchool | IsSuperAdmin])
def get_school_teachers(request, pk):
    print(request.user)
    school = get_object_or_404(School, _id=pk)
    print(school.admin)
    teachers = school.teachers.all()
    serializer = TeacherSerializer(teachers, many=True)  # Serialize the teachers data
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsSchoolAdminOfSchool | IsSuperAdmin])
def get_school_iteachers(request):
    if request.method == 'POST':
        print(request.user.role)
        school_id = request.data.get('school_id')
        if not school_id:
            return Response({'error': 'School ID missing in request'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            school = School.objects.get(_id=school_id)
            teachers = school.teachers.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(['GET'])
# @permission_classes([IsSchoolAdminOfSchool | IsSuperAdmin])
# def get_school_teachers(request):
#     school = request.school  # Use the school stored in the request object by the permission class
#     print(request.user)
#     print(school.admin)
#     teachers = school.teachers.all()
#     serializer = TeacherSerializer(teachers, many=True)  # Serialize the teachers data
#     return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsSchoolAdminOfSchool])
def get_teacher_of_school(request):
    if request.method == 'POST':
        school_id = request.data.get('school_id')
        teacher_id = request.data.get('teacher_id')
        if not school_id or not teacher_id:
            return Response({'error': 'School ID or Teacher ID missing in request'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            school = School.objects.get(_id=school_id)
            teacher = school.teachers.get(_id=teacher_id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found in the specified school'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)