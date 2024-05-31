from celery import shared_task

from habits.services import remind_of_habit


@shared_task
def habit_track(habit):
    """
    Таск Celery для напоминания о выполнении привычки
    """
    remind_of_habit(habit)
