from rest_framework import generics
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserRegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=response.data["email"])

        # Генерация JWT токенов
        refresh = RefreshToken.for_user(user)
        response.data["refresh"] = str(refresh)
        response.data["access"] = str(refresh.access_token)

        return response

