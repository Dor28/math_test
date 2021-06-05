from django.core.exceptions import ValidationError
from math_test.models import Problem, Task, TaskProblem, Theme, Tutor
from rest_framework import serializers
from datetime import datetime


class ProblemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('description', 'title', 'answer', 'helper', 'prompt', 'condition')

    def validate(self, attrs):
        user = self.context['request'].user
        if not hasattr(user, 'tutor'):
            raise ValidationError({'detail': 'Вы не являетесь учителем'})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['tutor'] = self.context['request'].user.tutor
        return super().create(validated_data)


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('description', 'title', 'answer', 'helper', 'prompt', 'condition')

    def to_representation(self, instance: Problem):
        response = super().to_representation(instance)
        tutor = Tutor.objects.get(id=instance.tutor.id)
        response['tutor'] = tutor.user.get_full_name()

        return response


class TaskSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('expiration', 'description', 'title', 'tutor', 'group', 'problem')

    def validate(self, attrs):
        user = self.context['request'].user
        if not hasattr(user, 'tutor'):
            raise ValidationError({'detail': 'Вы не являетесь учителем'})

        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['tutor'] = self.context['request'].user.tutor
        return super().create(validated_data)


class ThemeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('description', 'title', 'answer')

    def validate(self, attrs):
        user = self.context['request'].user
        if not hasattr(user, 'tutor'):
            raise ValidationError({'detail': 'Вы не являетесь учителем'})

        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['tutor'] = self.context['request'].user.tutor
        return super().create(validated_data)


class TaskProblemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskProblem
        fields = ('problem', 'task')


class TaskReceiveListSerializer(serializers.ModelSerializer):
    problem = ProblemListSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = ('expiration', 'description', 'title', 'tutor', 'group', 'problem')

    def to_representation(self, instance: Task):
        response = super().to_representation(instance)
        tutor = Tutor.objects.get(id=instance.tutor.id)
        response['tutor'] = tutor.user.get_full_name()

        return response
