from django.urls import path
from core.views.students_views import *

urlpatterns = [
    # ... other URL patterns
    path('number_of_students/', getNumberOfStudents, name='numbers-students'),
    path('<int:student_id>/semesters-scores/', student_semesters_scores, name='student-semesters-scores'),
]