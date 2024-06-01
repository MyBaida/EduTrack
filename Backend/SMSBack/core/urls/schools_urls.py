from django.urls import path
from core.views.schools_views import *

urlpatterns = [
    path('create/', create_school_with_admin, name='create_school_with_admin'),
]
