from django.urls import path
from core.views.users_views import *

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', getUsers, name='users'),
    path('profile/', getUserProfile, name='user-profile'),
    path('<str:pk>/', getUserById, name='user'),
]