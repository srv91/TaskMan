from django.forms import widgets
from rest_framework import serializers
from ellipse.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('taskname', 'deadline', 'user')

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email')

