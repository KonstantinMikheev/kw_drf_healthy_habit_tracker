from  rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.sesrializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def perform_create(self, serializer):
        """Переопределение метода для автоматической привязки владельца к создаваемому объекту."""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Возвращает объекты владельца и публичные объекты."""
        return Habit.objects.filter(user=self.request.user)


    def get_permissions(self):
        """Возвращает список разрешений, требуемых для пользователей группы moderators."""
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "retrieve", "list", "destroy"]:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class HabitsPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = HabitPagination
