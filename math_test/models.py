from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import AutoField
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import AutoField
from django.contrib.auth.models import AbstractUser


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Group(Base):
    title = models.CharField(max_length=32)
    access_mode = models.CharField(max_length=32)
    invite_link = models.URLField()


class Student(Base):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    group = models.ManyToManyField('Group', )


class Tutor(Base):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    group = models.ManyToManyField('Group')


class Theme(Base):
    description = models.TextField()
    title = models.TextField()
    answer = models.TextField()
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE)


class Task(Base):
    expiration = models.DateField()
    description = models.TextField()
    title = models.TextField()
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    problem = models.ForeignKey("Problem", on_delete=models.CASCADE)


class TaskProblem(Base):
    problem = models.ForeignKey("Problem", on_delete=models.CASCADE)
    task = models.ManyToManyField("Task")


class Problem(Base):
    condition = models.TextField(default="")
    prompt = models.TextField(default="")
    helper = models.TextField(default="")
    description = models.TextField()
    title = models.TextField()
    answer = models.TextField(default="")
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE)
