from django.urls import path
from . import views


urlpatterns = [
   #---------------POST--------------
   path('problem/create/', views.ProblemCreateView.as_view()),
   path('task/send/', views.TaskSendCreateView.as_view()),
   path('theme/create/', views.ThemeCreateView.as_view()),
   path('task_problem/create/', views.TaskProblemCreateView.as_view()),

   #--------------GET------------------
   path('task/list/', views.TaskReceiveListView.as_view()),

]