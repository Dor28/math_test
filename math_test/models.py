from django.db import models
from django.db.models.fields import AutoField
from django.contrib.auth.models import AbstractUser

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstarct = True



class User(AbstractUser):
    username = models.CharField(max_length=25,
                                unique=True,
                                error_messages={
                                     'unique':("A user with that phone already exists."),
                                }
                               )

    is_teacher = models.BooleanField(default=False)



class Theme(Base):
    title = models.CharField(max_length=255)


class Problem(Base):
    type = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    right_answer = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    theme = models.ForeignKey(Theme, models.CASCADE)

class Group(Base):
    name = models.CharField(max_length=255)



class Test(Base):
    start_date = models.DateField()
    task = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    end_date = models.DateField()










