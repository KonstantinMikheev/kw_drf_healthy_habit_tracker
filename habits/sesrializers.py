from rest_framework import serializers
from habits.models import Habit
from rest_framework.validators import UniqueValidator

from habits.validators import FrequencyValidator, ExecuteTimeValidator, RelatedAndIsGoodValidator, \
    RewardAndRelatedValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        validators = [
            UniqueValidator(
                queryset=Habit.objects.all(),
                message='Извините, но у вас уже есть такая привычка.'
            ),
            RewardAndRelatedValidator(),
            FrequencyValidator(),
            ExecuteTimeValidator(),
            RelatedAndIsGoodValidator(),
            ]
