from django.urls import path
from . import views


urlpatterns = [
   path('problem/create/', views.ProblemCreateView.as_view()),
]