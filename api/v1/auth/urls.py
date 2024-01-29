from django.urls import path
from django.urls.conf import include
from . import views



urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('student/create', views.StudentCreateView.as_view()),
    path('tutor/create/', views.TeacherCreateView.as_view())
    
]