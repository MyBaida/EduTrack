from django.urls import path
from core.views.classes_views import *

urlpatterns = [
    path('', getClasses, name='get-classes'),
    path('add/', createClass, name='add-class'),
    path('<int:pk>/', getClass, name='get-class'),
    path('<int:class_id>/semester/<int:semester_id>/top-students/', top_students_view, name='top-students'),
    path('<int:class_id>/semester/<int:semester_id>/subject-statistics/', get_subject_grade_statistics, name='subject-grade-statistics'),
]

