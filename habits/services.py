import json

import requests
from django.utils import timezone
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from config.settings import TELEGRAM_API
from habits.models import Habit


def send_tg_message(message, chat_id):
    """    Отправка сообщения в Telegram    """
    params = {
        'text': message,
        'chat_id': chat_id
    }
    try:
        response = requests.get(f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage', params=params)
        response.raise_for_status()
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


def remind_of_habit(habit_id):
    """
    Напоминание о выполнении привычки
    """
    habit = Habit.objects.get(pk=habit_id)
    if habit.user.chat_id:
        message = f'''Привет!\nНе забудь сегодня выполнить привычку:"{habit.action}" в {habit.time.strftime("%H:%M")} 
        Место: {habit.place}'''
        send_tg_message(message, habit.user.chat_id)


def create_periodic_task(habit):
    """
    Создание периодической задачи Celery
    """
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=habit.periodicity,
        period=IntervalSchedule.DAYS,
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name=f'Send Habit {habit.pk} notification',
        task='habits.tasks.habit_reminder',
        kwargs=json.dumps({
            'habit_id': habit.pk,
        }),
        start_time=timezone.now()
    )
