from datetime import datetime
import json

from django.core import serializers

from tasks.models import Task, States


class TaskManager:
    def __init__(self, request, name=None):
        self.user = request.user
        self.tasks = Task.objects.filter(user=self.user)
        if name:
            self.filtered_task = self.tasks.filter(name=name)

    def __get_datetime(self):
        return str(datetime.now())

    def check_task_exists(self, name):
        return True if self.tasks.filter(name=name) else False

    def create(self, name, description, finish_time):
        task = Task(name=name, description=description, finish_time=finish_time, user=self.user)
        task.save()
        data = serializers.serialize('json', [task, ])
        return data

    def change_name(self, to_change_name):
        json_history = self.filtered_task[0].name_history
        json_history[self.__get_datetime()] = to_change_name
        self.filtered_task.update(name_history=json_history, name=to_change_name)
        data = serializers.serialize('json', [self.tasks.filter(name=to_change_name)[0], ])
        return data

    def change_description(self, to_change_description):
        json_history = self.filtered_task[0].description_history
        json_history[self.__get_datetime()] = to_change_description
        self.filtered_task.update(description_history=json_history, description=to_change_description)
        data = serializers.serialize('json', [self.filtered_task[0], ])
        return data

    def change_finish_time(self, to_change_finish_time):
        json_history = self.filtered_task[0].finish_time_history
        json_history[self.__get_datetime()] = to_change_finish_time
        self.filtered_task.update(finish_time_history=json_history, finish_time=to_change_finish_time)
        data = serializers.serialize('json', [self.filtered_task[0], ])
        return data

    def change_state(self, to_change_state):
        if to_change_state in States.__members__:
            json_history = self.filtered_task[0].state_history
            json_history[self.__get_datetime()] = to_change_state
            self.filtered_task.update(state_history=json_history, state=to_change_state)
            data = serializers.serialize('json', [self.filtered_task[0], ])
            return data
        raise KeyError

    def show_tasks(self, filter):
        tasks = self.tasks.filter(**filter).all()
        data = serializers.serialize('json', tasks)
        return data

    def show_history(self):
        history = self.filtered_task.all().values('state_history', 'description_history', 'finish_time_history', 'name_history')[0]
        data = json.dumps(history)
        return data

