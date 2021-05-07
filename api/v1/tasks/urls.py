from django.urls import path
from . import views


urlpatterns = [
   path('problem/create/', views.ProblemCreateView.as_view()),
   path('task/send/', views.TaskSendCreateView.as_view()),
   path('theme/create/', views.ThemeCreateView.as_view()),
   path('task_problem/create/', views.TaskProblemCreateView.as_view()),
]