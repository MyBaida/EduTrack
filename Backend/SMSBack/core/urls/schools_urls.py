from django.urls import path
from core.views.schools_views import *

urlpatterns = [
    path('create/', create_school_with_admin, name='create_school_with_admin'),
    path('<int:pk>/teachers/', get_school_teachers, name='get-school-teachers'),
    path('teachers/', get_school_iteachers, name='get-school-teachers'),
    path('teacher/', get_teacher_of_school, name='school-teacher')
]
