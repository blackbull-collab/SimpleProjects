from django.urls import path
from . import views

app_name="task"

urlpatterns = [
    path("task_list",views.task_list,name="tasklist"),
    path("task_detail",views.task_detail,name="taskdetail"),
    path("create_task",views.create_task,name="createtask"),
    path("edit_task",views.edit_task,name="edittask")
]
