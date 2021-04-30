from django.contrib import admin
from math_test.models import  (User, Group,  Problem, TaskProblem,Theme, Task, Tutor, Student)

admin.site.register(User)

admin.site.register(Problem)

admin.site.register(TaskProblem)


admin.site.register(Task)


admin.site.register(Tutor)

admin.site.register(Student)


admin.site.register(Group)

