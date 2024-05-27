from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginators import Pagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """

        new_habit = serializer.save(user=self.request.user)


class HabitsListAPIView(generics.ListAPIView):
    """ Вывод списка привычек пользователя """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class HabitsPublicListAPIView(generics.ListAPIView):
    """ Вывод списка публичных привычек """

    serializer_class = HabitSerializer
    pagination_class = Pagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр информации об одной привычке """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """ Изменение привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
