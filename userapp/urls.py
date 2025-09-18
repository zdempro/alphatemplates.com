# userapp/urls.py
from django.urls import path
from .generics import UserRegisterApiView

urlpatterns = [
    path("register/", UserRegisterApiView.as_view(), name="api-register"),
]
