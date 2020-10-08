# Generated by Django 3.1.2 on 2020-10-08 18:46

import datetime
from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 18, 46, 20, 641502)),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('Новая', 'NEW'), ('В работе', 'IN_PROGRESS'), ('Завершенная', 'DONE')], default=tasks.models.States['NEW'], max_length=12),
        ),
    ]
