from math_test.permissions import TeacherPermission
from api.v1.tasks.serializers import ProblemCreateSerializer, TaskSendSerializer, ThemeCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView


class ProblemCreateView(CreateAPIView):
    serializer_class = ProblemCreateSerializer
    permission_classes = [TeacherPermission, ]


class TaskSendCreateView(CreateAPIView):
    serializer_class = TaskSendSerializer
    permission_classes = [TeacherPermission, ]


class ThemeCreateView(CreateAPIView):
    serializer_class = ThemeCreateSerializer
    permission_classes = [TeacherPermission, ]

