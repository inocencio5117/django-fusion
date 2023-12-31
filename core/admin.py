from django.contrib import admin

from .models import Role, Employee, Service

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'active', 'created_at', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at', 'updated_at')