from django.urls import path
from core.views.teachers_views import *

urlpatterns = [
    path('', getTeachers, name='teachers'),
    path('number_of_teachers/', getNumberOfTeachers, name='numbers-teachers'),
    path('<int:pk>/', getTeacher, name='teacher'),
]