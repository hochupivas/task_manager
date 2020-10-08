from datetime import datetime

from django.db import models
from enum import Enum
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class States(Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Task(models.Model):
    NOW = str(datetime.now())

    def json_field(self, value):
        return {self.NOW: value}

    name = models.CharField(max_length=500, unique=True)
    name_history = JSONField()
    description = models.CharField(max_length=1000)
    description_history = JSONField()
    state = models.CharField(choices=States.choices(), default="NEW", max_length=12)
    state_history = JSONField()
    start_time = models.DateTimeField(default=datetime.now())
    finish_time = models.DateField()
    finish_time_history = JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        if not self.id and not self.finish_time_history:
            self.finish_time_history = self.json_field(str(self.finish_time))
        if not self.id and not self.state_history:
            self.state_history = self.json_field(self.state)
        if not self.id and not self.name_history:
            self.name_history = self.json_field(self.name)
        if not self.id and not self.description_history:
            self.description_history = self.json_field(self.description)
        return super(Task, self).save(*args, **kwargs)
