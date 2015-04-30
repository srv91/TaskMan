from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.db import connection
from django.contrib.auth.models import User
from ellipse.models import Task, Useractivity
import requests

def loginpage(request):
    return render(request, 'ellipse/loginpage.html')

def dashboard(request):
    if request.POST.get('username') and request.POST.get('password') and request.POST.get('email'):
        e_name = request.POST.get('username')
        e_pass = request.POST.get('password')
        e_mail = request.POST.get('email')

        user = authenticate(username = e_name, password = e_pass, email = e_mail)
        if user is not None:
            emp = User.objects.get(username = e_name)
            if user.is_active:
                login(request, user)
                my_tasks = Task.objects.filter(user=emp)
                if my_tasks:
                    return render(request, 'ellipse/dashboard.html', {'employee':emp, 'tasks':my_tasks})
                else:
                    emp = User.objects.get(id = request.user.id)
                    return render(request, 'ellipse/dashboard.html', {'employee':emp})
        else:
            return render(request, 'ellipse/dashboard.html')
    else:
        emp = User.objects.get(id = request.user.id)
        my_tasks = Task.objects.filter(user=emp)
        return render(request, 'ellipse/dashboard.html', {'employee':emp, 'tasks':my_tasks})

def manage(request):
    if request.POST.get('taskname'):
        name = request.POST.get('taskname')
        end = request.POST.get('enddate')
        emp = User.objects.get(id = request.user.id)
        print emp.username
        newtask = Task(user = emp, taskname = name, deadline = end, completed = False)
        newtask.save()
        newact = Useractivity(user = emp, flag = 1, obj = name)
        newact.save()
        my_tasks = Task.objects.filter(user = emp)
        return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

    else:
        selected = request.POST.get('dropdown')
        if selected == 'Delete':
            tasks = request.POST.getlist('t')
            emp = User.objects.get(id = request.user.id)
            for seltask in tasks:
                deltask = Task.objects.get(user = emp, id = seltask)
                newact = Useractivity(user = emp, flag = 2, obj = deltask.taskname)
                newact.save()
                deltask.delete()
            my_tasks = Task.objects.filter(user = emp)
            return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

        elif selected == 'Mark as complete':
            ctasks = request.POST.getlist('t')
            emp = User.objects.get(id = request.user.id)
            for seltask in ctasks:
                mtask = Task.objects.filter(user = emp, id = seltask)
                mtask.update(completed = True)
            my_tasks = Task.objects.filter(user = emp)
            return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

        elif selected == 'Mark as incomplete':
            itasks = request.POST.getlist('t')
            emp = User.objects.get(id = request.user.id)
            for seltask in itasks:
                mtask = Task.objects.filter(user = emp, id = seltask)                
                mtask.update(completed = False)
            my_tasks = Task.objects.filter(user = emp)
            return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

        elif selected == 'Sort in name':
            emp = User.objects.get(id = request.user.id)
            my_tasks = Task.objects.order_by('taskname')
            return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

        elif selected == 'Sort in date added':
            emp = User.objects.get(id = request.user.id)
            my_tasks = Task.objects.order_by('added_on')
            return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

        elif selected == 'Sort in deadlines':
            emp = User.objects.get(id = request.user.id)
            my_tasks = Task.objects.order_by('deadline')
            return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

    emp = User.objects.get(id=request.user.id)
    my_tasks = Task.objects.filter(user=emp)
    return render(request, 'ellipse/dashboard.html', {'employee': emp, 'tasks': my_tasks})

def useractivity(request, user_id):
    emp = User.objects.get(id = user_id)
    act = Useractivity.objects.filter(user=emp)
    return render(request, 'ellipse/useractivity.html', {'log': act})

