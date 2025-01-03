from django.urls import path
from core.views.semesters_views import *

urlpatterns = [
    path('', getSemesters, name='get-semesters'),
    path('add/', createSemester, name='add-semester'),
    path('<int:pk>/subjects/', semester_subjects, name='semester-subjects'),
    path('<int:pk>/', getSemester, name='get-semester')
]