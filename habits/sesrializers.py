from rest_framework import serializers
from habits.models import Habit
from rest_framework.validators import UniqueValidator

from habits.validators import FrequencyValidator, ExecuteTimeValidator, RelatedAndIsGoodValidator, \
    RewardAndRelatedValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardAndRelatedValidator(),
            FrequencyValidator(),
            ExecuteTimeValidator(),
            RelatedAndIsGoodValidator(),
        ]
