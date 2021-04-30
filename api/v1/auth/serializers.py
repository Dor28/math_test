from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return super().create(validated_data)

