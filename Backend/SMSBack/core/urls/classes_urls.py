from django.urls import path
from core.views.classes_views import *

urlpatterns = [
    path('', getClasses, name='get-classes'),
    path('add/', createClass, name='add-class'),
    path('<int:pk>/', getClass, name='get-class')
]

