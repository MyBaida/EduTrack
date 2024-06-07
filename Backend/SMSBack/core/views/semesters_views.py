from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser 

from core.models import Semester, Subject, School
from core.serializers import SemesterSerializer
from core.permissions import IsSuperAdmin, IsSchoolAdmin, IsTeacher, IsTeacherOfSubject, IsSchoolAdminOfSchool


from rest_framework import status


@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def getSemesters(request):
    try:
        school = request.user.managed_school
    except School.DoesNotExist:
        return Response({'error': 'School not found for the current admin'}, status=status.HTTP_404_NOT_FOUND)

    # Get all subjects linked to the school
    subjects = Subject.objects.filter(school=school)
    
    # Get all semesters linked to the subjects of the school
    semesters = Semester.objects.filter(subjects__in=subjects).distinct()
    
    serializer = SemesterSerializer(semesters, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def getSemester(request, pk):
    semester = Semester.objects.get(_id=pk)
    serializer = SemesterSerializer(semester, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsSchoolAdmin])
def createSemester(request):
    if request.method == 'POST':
            serializer = SemesterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)