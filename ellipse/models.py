from django.db import models
from django.contrib.auth.models import User
import django
import datetime

class Task(models.Model):
    user = models.ForeignKey(User,null=True)
    taskname = models.CharField(max_length = 100, default='not defined')
    added_on = models.DateField(default=datetime.datetime.now)
    deadline = models.DateField(default=datetime.datetime.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskname

class Useractivity(models.Model):
    user = models.ForeignKey(User,null=True)
####flags : Add-1, Delete-2
    flag = models.IntegerField(default=0)
    obj = models.CharField(max_length=100,default='unknown')

    def __str__(self):
        return self.user.username

