from django.urls import path
from . import views

urlpatterns = [
    path("task_list",views.task_list,name="tasklist"),
    path("task_detail",views.task_detail,name="taskdetail"),
    path("create_task",views.create_task,name="createtask"),
    path("edit_task",views.edit_task,name="edittask")
]
