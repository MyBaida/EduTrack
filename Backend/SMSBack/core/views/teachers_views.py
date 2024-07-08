from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from core.models import Teacher

from core.permissions import *
from rest_framework import status

from core.serializers import TeacherSerializer


@api_view(['GET'])
@permission_classes([IsSuperAdmin])
def getTeachers(request):
    teachers= Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def getNumberOfTeachers(request):
    try:
        school = request.user.managed_school
    except School.DoesNotExist:
        return Response({'error': 'School not found for current admin'}, status=status.HTTP_404_NOT_FOUND)
    teachers= Teacher.objects.filter(school=school).count()
    return Response(teachers)

@api_view(['GET'])
@permission_classes([IsSuperAdmin])
def getTeacher(request, pk):
    teacher = Teacher.objects.get(_id=pk)
    serializer = TeacherSerializer(teacher, many=False)
    return Response(serializer.data)
    