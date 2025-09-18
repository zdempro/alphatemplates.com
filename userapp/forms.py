from django import forms
from unfold.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "email", "password1", "password2")  # 👈 email включаем как поле модели


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("name", "email", "first_name", "last_name", "is_active", "is_staff")
