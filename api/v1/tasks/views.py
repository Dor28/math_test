from math_test.permissions import TeacherPermission
from api.v1.tasks.serializers import ProblemCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView


class ProblemCreateView(CreateAPIView):
    serializer_class = ProblemCreateSerializer
    permission_classes = [TeacherPermission, ]

