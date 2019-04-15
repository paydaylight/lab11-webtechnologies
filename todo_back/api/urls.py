from django.urls import path

from . import views

urlpatterns = [
    path('task_lists/', views.task_lists, name='task_lists'),
    path('task_lists/<int:id>/', views.task_list_detail, name='task_list_details'),
    path('task_lists/<int:id>/tasks/', views.tasks_for_task_list, name='tasks'),
    path('tasks/<int:id>/', views.task, name='task')
]