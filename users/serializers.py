from rest_framework import serializers
from django.contrib.auth.models import User

# ------------------------
# Регистрация
# ------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')
        extra_kwargs = {'password': {'write_only': True}}

    # Проверка паролей
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    # Создание пользователя
    def create(self, validated_data):
        validated_data.pop('password_confirm')  # убираем лишнее поле
        user = User.objects.create_user(**validated_data)  # создаём через create_user
        return user


# ------------------------
# Просмотр пользователей
# ------------------------
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

    # Проверка username
    def validate_username(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя пользователя не может быть пустым")
        return value

    # Проверка email
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email уже используется")
        return value
