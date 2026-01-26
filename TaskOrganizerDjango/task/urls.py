from django.urls import path
from . import views

app_name="task"

urlpatterns = [
    path("task_list",views.task_list,name="tasklist"),
    path("task_detail/<int:task_id>/",views.task_detail,name="taskdetail"),
    path("create_task",views.create_task,name="createtask"),
    path("edit_task/<int:task_id>/",views.edit_task,name="edittask"),
    path("delete_task/<int:task_id>/",views.delete_task,name="deletetask")
]
