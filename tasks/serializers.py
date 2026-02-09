from rest_framework import serializers
from datetime import date
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"  # обязательно двойное подчёркивание
        read_only_fields = ["owner", "created_at", "updated_at"]

    # 🔹 Проверка title
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым")
        return value

    # 🔹 Проверка description
    def validate_description(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Описание должно быть минимум 8 символов")
        return value

    # 🔹 Проверка дедлайна
    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError("Дата выполнения не может быть в прошлом")
        return value

    # 🔹 Общая проверка (если понадобится)
    def validate(self, data):
        return data
