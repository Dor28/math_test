from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('user/', include("api.v1.auth.urls") ),
    path('tutor/', include("api.v1.tasks.urls"))
]