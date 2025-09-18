from django.contrib import admin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.utils.translation import gettext_lazy as _
from .models import User
from . import forms

admin.site.unregister(Group)



@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = forms.CustomUserChangeForm
    add_form = forms.CustomUserCreationForm
    change_password_form = AdminPasswordChangeForm
     
    list_display = ['name','email','date_joined','last_login','is_active','is_staff','is_superuser']
    ordering =['email']
    fieldsets = (
        (None, {"fields": ("email", "name", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2", "is_active", "is_staff", "is_superuser"),
        }),
    )

    


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass