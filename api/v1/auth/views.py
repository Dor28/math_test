from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import StudentCreateSerializer, TeacherCreateSerializer, UserCreateSerializer

User = get_user_model()



class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny, )

    
class StudentCreateView(CreateAPIView):
    serializer_class = StudentCreateSerializer
    permission_classes = (AllowAny, )


class TeacherCreateView(CreateAPIView):
    serializer_class = TeacherCreateSerializer
    permission_classes = (AllowAny, )


