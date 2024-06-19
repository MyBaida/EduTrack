from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Grade, Semester, Student
from rest_framework.decorators import api_view, permission_classes
from core.permissions import IsSuperAdmin, IsSchoolAdmin, IsTeacher, IsTeacherOfSubject, IsSchoolAdminOfSchool


@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def student_semesters_scores(request, student_id):
    try:
        student = Student.objects.get(_id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Invalid student ID'}, status=404)

    semesters = Semester.objects.all()
    student_scores = []

    for semester in semesters:
        total_score = Grade.objects.filter(student=student, semester=semester).aggregate(total_score=Sum('score'))['total_score'] or 0
        student_scores.append({
            'semester_name': semester.name,
            'total_score': total_score
        })

    student_data = {
        'student_name': f"{student.first_name} {student.last_name}",
        'student_id': student._id,
        'semester_scores': student_scores
    }

    return Response(student_data)