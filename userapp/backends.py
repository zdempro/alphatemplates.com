from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    """Аутентификация по email вместо username"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # username = email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
