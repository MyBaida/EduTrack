from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from core.models import Teacher

from core.permissions import *

from core.serializers import TeacherSerializer


@api_view(['GET'])
@permission_classes([IsSuperAdmin])
def getTeachers(request):
    teachers= Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsSuperAdmin])
def getTeacher(request, pk):
    teacher = Teacher.objects.get(_id=pk)
    serializer = TeacherSerializer(teacher, many=False)
    return Response(serializer.data)
    