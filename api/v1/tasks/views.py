from math_test.models import Student, Task, TaskProblem,Tutor
from re import L
from math_test.permissions import TeacherPermission
from api.v1.tasks.serializers import ProblemCreateSerializer, TaskProblemCreateSerializer, TaskReceiveListSerializer, TaskSendSerializer, ThemeCreateSerializer
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


class TaskProblemCreateView(CreateAPIView):
    serializer_class = TaskProblemCreateSerializer
    permission_classes = [TeacherPermission,]


class TaskReceiveListView(ListAPIView):
    serializer_class = TaskReceiveListSerializer
    
    def get_queryset(self):
        user_from_request = self.request.user
        qs = Tutor.objects.all()
        if hasattr(user_from_request, 'student'):
            student = Student.objects.get(user=user_from_request)
            group = student.group.last()
            qs = qs.filter(group=group)
        if hasattr(user_from_request, 'teacher'):
            teacher = Tutor.objects.filter(user=user_from_request)
            qs = qs.filter(tutor=teacher)
        return qs