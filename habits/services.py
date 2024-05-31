import requests
from datetime import datetime as dt
from django.utils import timezone
from django_celery_beat.models import IntervalSchedule, PeriodicTask, CrontabSchedule
from django_celery_beat.utils import make_aware

from config.settings import TELEGRAM_API

periodicity = {
        1: IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.DAYS),
        2: CrontabSchedule.objects.get_or_create(day_of_week='1-5'),
        3: CrontabSchedule.objects.get_or_create(day_of_week='6-7'),
        4: IntervalSchedule.objects.get_or_create(every=7, period=IntervalSchedule.DAYS),
    }

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


def remind_of_habit(habit):
    """
    Напоминание о выполнении привычки
    """
    if habit.user.chat_id:
        message = f'''Привет!\nНе забудь сегодня выполнить привычку:"{habit.action}" в {habit.time.strftime("%H:%M")}'''
        '''Место: {habit.place}'''
        send_tg_message(message, habit.user.chat_id)


def create_periodic_task(habit):
    """
    Создание периодической задачи Celery
    """
    start = timezone.now().strftime("%d.%m.%Y") + habit.time.strftime(" %H:%M:%S")
    star = dt.strptime(start, '%d.%m.%Y %H:%M:%S')
    sta = make_aware(star)

    PeriodicTask.objects.create(
        interval=periodicity[habit.periodicity][0] if habit.periodicity in (1, 4) else None,
        crontab=periodicity[habit.periodicity][0] if habit.periodicity in (2, 3) else None,
        name=f'{habit.pk}',
        task='habits.tasks.habit_reminder',
        start_time=sta
    )
