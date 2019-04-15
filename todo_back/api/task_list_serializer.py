from django.core.serializers.python import Serializer
from django.core.serializers import json


class TaskListSerializer(json.Serializer):
    def get_dump_object(self, obj):
        self._current['id'] = obj.id
        self._current['name'] = obj.name
        return self._current
