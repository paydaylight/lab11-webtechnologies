from django.http import HttpResponse
from .models import TaskList, Task
from .task_list_serializer import TaskListSerializer
from .task_serializer import TaskSerializer
# Create your views here.


def task_lists(request):
    task_lists = TaskList.objects.all()
    serializer = TaskListSerializer()
    to_json = serializer.serialize(task_lists)
    return HttpResponse(to_json, content_type='application/json')


def task_list_detail(request, id):
    task_list = TaskList.objects.get(id=id)
    serializer = TaskListSerializer()
    json_response = serializer.serialize([task_list])
    return HttpResponse(json_response, content_type='application/json')


def tasks_for_task_list(request, id):
    tasks = Task.objects.filter(pk=id)
    serializer = TaskSerializer()
    json_response = serializer.serialize(tasks, fields=('id', 'name', 'status'))
    return HttpResponse(json_response, content_type='application/json')


def task(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer()
    json_response = serializer.serialize([task])
    return HttpResponse(json_response, content_type='application/json')