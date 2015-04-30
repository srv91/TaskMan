from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ellipse.models import Task
from comet.serializers import TaskSerializer
from rest_framework import permissions
from django.http import HttpResponse

@api_view(['GET', 'POST'])
def task_view(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
##### To check ids
        for t in tasks:
            print t.id
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.update(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def task_del(request, task_id):

    if request.method == 'DELETE':
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_204_NO_CONTENT)

