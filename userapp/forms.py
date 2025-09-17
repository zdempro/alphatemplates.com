from django import forms
from django.contrib.auth.forms import AuthenticationForm
from unfold.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email", 
        widget=forms.TextInput(attrs={"autofocus": True})
    )

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

