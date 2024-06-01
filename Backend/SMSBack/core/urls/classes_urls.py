from django.urls import path
from core.views.classes_views import *

urlpatterns = [
    path('add/', createClass, name='add-class'),
]

