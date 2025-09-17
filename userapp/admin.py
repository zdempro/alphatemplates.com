from django.contrib import admin
from django.contrib.auth.models import User,Group
from userapp.forms import EmailAuthenticationForm
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from . import forms
admin.site.login_form = EmailAuthenticationForm

admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = forms.CustomUserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ['username','email','date_joined'] 
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass