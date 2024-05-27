"""
URL configuration for SMSBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/classes/', include('core.urls.classes_urls')),
    path('api/schools/', include('core.urls.schools_urls')),
    path('api/users/', include('core.urls.users_urls')),
    # path('api/teachers/', include('core.urls.teachers_urls')),
    # path('api/grades/', include('core.urls.grades_urls')),
    # path('api/subjects/', include('core.urls.subjects_urls')),
    # path('api/semesters/', include('core.urls.semesters_urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
