from django.core.exceptions import ValidationError
from math_test.models import Problem
from rest_framework import serializers


class ProblemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('description', 'title', 'answer')

    
    def validate(self, attrs):
        user = self.context['request'].user
        if not hasattr(user, 'tutor'):
            raise ValidationError({'detail':'Вы не являетесь учителем'})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['tutor'] = self.context['request'].user.tutor
        return super().create(validated_data)