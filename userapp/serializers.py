from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate
User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    
    class Meta:
        model = User
        fields = ['name','email','password']

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Пароль должен содержать минимум 6 символов.")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs['email'],password=attrs['password'])
        
        if not user:
            raise serializers.ValidationError("Неверный email или пароль")
        
        if not user.is_active:
            raise serializers.ValidationError("Аккаунт деактивирован")
        
        attrs['user']=user

        return attrs
    
class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()