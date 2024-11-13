from  rest_framework import viewsets

from habits.models import Habit
from habits.sesrializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
