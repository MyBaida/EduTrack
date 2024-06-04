from django.urls import path
from core.views.grades_views import *

urlpatterns = [
    path('class/<int:class_id>/semester/<int:semester_id>/', get_class_grades, name='get_class_grades'),
     path('class/<int:class_id>/subject/<int:subject_id>/semester/<int:semester_id>/', get_class_subject_grades, name='get_class_subject_grades'),
]
