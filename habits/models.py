from datetime import timedelta

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):
    PERIODICITY_CHOICES = [
        (1, 'Каждый день'),
        (2, 'Каждую неделю'),
        (3, 'Каждый будний день'),
        (4, 'Каждые выходные')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user',
                             verbose_name='Пользователь')
    place = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=300, verbose_name='Действие')
    is_nice = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, related_name='main_habit',
                                      verbose_name='Связанная привычка')
    periodicity = models.PositiveIntegerField(default=1, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')
    reward = models.CharField(max_length=300, **NULLABLE, verbose_name='Вознаграждение')
    duration = models.DurationField(verbose_name='Длительность выполнения',
                                    validators=[MaxValueValidator(timedelta(seconds=120))])
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('pk',)
