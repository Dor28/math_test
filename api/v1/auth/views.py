from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer

User = get_user_model()



class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializers = UserCreateSerializer
    permission_classes = (AllowAny,)