from celery import shared_task
from datetime import datetime
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def habits_telegram_notification():
    """Функция отправки уведомления о повторении дел в Telegram."""
    habits = Habit.objects.all()
    current_date = datetime.now()  # Текущее время
    for habit in habits:
        if habit.time >= current_date:
            chat_id = habit.user.tg_chat_id
            message = f"Настало время {habit.action} в {habit.place}."
            send_telegram_message(chat_id, message)  # Отправляем привычку в Telegram чат
