from django.contrib.auth import get_user_model
from math_test.models import Student, Tutor
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('group',)

    def create(self,validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('group',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
        

