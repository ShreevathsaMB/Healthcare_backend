from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Patient, Doctor, PatientDoctorMapping


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_staff')
    ordering = ('email',)
    search_fields = ('email', 'name')


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientDoctorMapping)
