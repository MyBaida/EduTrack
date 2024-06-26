from django.urls import path
from core.views.students_views import student_semesters_scores

urlpatterns = [
    # ... other URL patterns
    path('<int:student_id>/semesters-scores/', student_semesters_scores, name='student-semesters-scores'),
]