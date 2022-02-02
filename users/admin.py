from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        ('Fill out bellow', {'fields': ('email', 'username', 'password')}),
    )
    list_display = ['id', 'username', 'email', 'date_joined', 'is_superuser', 'is_staff']
    list_per_page = 20
    list_display_links = ['username']
    list_editable = ['email', 'is_superuser', 'is_staff']
    list_filter = ['is_superuser', 'is_staff']
    ordering = ['id']
    search_fields = ['username', 'email']
    readonly_fields = ['date_joined', 'last_login']
    fieldsets = (
        ('General info', {'fields': ('username', 'email')}),
        ('Privacy', {'fields': ('password', )}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'user_permissions', 'groups')}),
        ('Important date', {'fields': ('date_joined', 'last_login')})
    )
