from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from core.models import Grade, Subject, Class, Semester
from core.serializers import GradeSerializer
from core.permissions import IsSchoolAdmin, IsTeacher
from core.utils import transform_grades

# @api_view(['GET'])
# @permission_classes([IsSchoolAdmin])
# def get_class_grades(request, class_id, semester_id):
#     try:
#         class_instance = Class.objects.get(_id=class_id)
#         semester_instance = Semester.objects.get(_id=semester_id)
#     except Class.DoesNotExist:
#         return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Semester.DoesNotExist:
#         return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)

#     students = class_instance.students.all()
#     grades = Grade.objects.filter(student__in=students, semester=semester_instance)

#     serializer = GradeSerializer(grades, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def get_class_grades(request, class_id, semester_id):
    try:
        class_instance = Class.objects.get(_id=class_id)
        semester_instance = Semester.objects.get(_id=semester_id)
    except Class.DoesNotExist:
        return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)

    students = class_instance.students.all()
    grades = Grade.objects.filter(student__in=students, semester=semester_instance)

    serializer = GradeSerializer(grades, many=True)
    transformed_data = transform_grades(serializer.data)
    
    return Response(transformed_data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def get_class_subject_grades(request, class_id, semester_id, subject_id):
    try:
        class_instance = Class.objects.get(_id=class_id)
        subject_instance = Subject.objects.get(_id=subject_id)
        semester_instance = Semester.objects.get(_id=semester_id)
    except Class.DoesNotExist:
        return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)

    students = class_instance.students.all()
    grades = Grade.objects.filter(student__in=students, subject=subject_instance, semester=semester_instance)

    serializer = GradeSerializer(grades, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
