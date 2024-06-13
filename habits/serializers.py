from rest_framework import serializers

from habits.models import Habit
from habits.validators import RewardValidator, RelatedHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализотор модели привычки"""
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['user']
        validators = [
            RewardValidator(field='reward'),
            RelatedHabitValidator(field='related_habit')
        ]
