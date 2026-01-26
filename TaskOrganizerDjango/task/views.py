from django.shortcuts import render
from .models import Task
# Create your views here.

alltasks=Task.objects.all()

def task_list(request):
    return render(request,"tasks/task_list.html",{"tasks":alltasks})

def task_detail(request,task_id):
    tasks=Task.objects.get(pk=task_id)
    return render(request,"tasks/task_detail.html",{"tasks":tasks})

def create_task(request):
    return render(request,"tasks/create_task.html",{"tasks":alltasks})

def edit_task(request,task_id):
    tasks=Task.objects.get(pk=task_id)
    return render(request,"tasks/edit_task.html",{"tasks":tasks})

def delete_task(request,task_id):
    tasks=Task.objects.get(pk=task_id)
    return render(request,"tasks/delete_task.html",{"tasks":tasks})