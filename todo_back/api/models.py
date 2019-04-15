from django.db import models
# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=50)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
