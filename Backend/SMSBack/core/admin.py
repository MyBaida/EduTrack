from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role', 'profile')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'profile')}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Grade)
