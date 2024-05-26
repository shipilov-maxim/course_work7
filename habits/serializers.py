from rest_framework import serializers

from habits.models import Habit
from habits.validators import RewardValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализотор модели привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [
            RewardValidator(field='reward'),
        ]
