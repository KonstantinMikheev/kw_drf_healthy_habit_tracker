from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель Habit для хранения информации о привычках пользователей."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
    )
    place = models.CharField(
        max_length=200,
        verbose_name="Место",
        help_text="Укажите место, в котором необходимо выполнять привычку",
        **NULLABLE,
    )
    time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Время",
        help_text="Укажите время, когда необходимо выполнять привычку",
        **NULLABLE,
    )
    action = models.CharField(
        max_length=200,
        verbose_name="Действие",
        help_text="Укажите действие, которое представляет собой привычку",
    )
    is_good_habit = models.BooleanField(default=False, verbose_name="Приятная привычка")
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    frequency = models.PositiveIntegerField(default=1, verbose_name="Периодичность")
    reward = models.CharField(
        max_length=200,
        verbose_name="Вознаграждение",
        help_text="Чем пользователь должен себя вознаградить после выполнения",
    )
    time_to_execute = models.TimeField(
        verbose_name="Время на выполнение",
        help_text="Время, которое предположительно потратит пользователь на выполнение привычки в минутах",
    )
    is_public = models.BooleanField(default=False, verbose_name="Публичность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
        ordering = ["-created_at"]


    def __str__(self):
        return f"""Кто: {self.user}, 
        Что должен сделать: {self.action}, 
        Когда: {self.time}, 
        Где: {self.place}, 
        Как часто: {self.frequency}"""
