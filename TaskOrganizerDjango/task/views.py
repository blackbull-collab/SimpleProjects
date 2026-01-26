from django.shortcuts import render

# Create your views here.

def task_list(request):
    return render(request,"tasks/task_list.html")

def task_detail(request):
    return render(request,"tasks/task_detail.html")

def create_task(request):
    return render(request,"tasks/create_tasks.html")

def edit_task(request):
    return render(request,"tasks/edit_tasks.html")