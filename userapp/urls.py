# userapp/urls.py
from django.urls import path
from . import generics
from rest_framework_simplejwt import views

urlpatterns = [
    path("register/", generics.UserRegisterApiView.as_view(), name="user-register"),
    path("login/",generics.UserLoginApiView.as_view(),name='user-login'),
    path('logout/',generics.UserLogoutApiView.as_view(),name ='user-logout'),
    path("token/", views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", views.TokenVerifyView.as_view(), name="token_verify"),
]
