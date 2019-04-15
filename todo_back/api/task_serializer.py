from django.core.serializers import json


class TaskSerializer(json.Serializer):
    def get_dump_object(self, obj):
        self._current['id'] = obj.id
        # self._current['name'] = obj.name
        # self._current['status'] = obj.status
        # self._current['created_at'] = obj.created_at
        # self._current['due_on'] = obj.due_on
        # self._current['task_list'] = obj.task_list
        return self._current
