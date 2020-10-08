import json
from dateutil import parser

from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from tasks.models import Task
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from tasks.task_managment import TaskManager


@csrf_exempt
@api_view(["GET"])
def home(request):
    return HttpResponse('Hello')


@csrf_exempt
@api_view(["POST"])
def task_create(request):
    task_manager = TaskManager(request)

    name = request.POST.get('name')
    description = request.POST.get('description')
    finish_time = parser.parse(request.POST.get('finish_time'))

    data = task_manager.create(name, description, finish_time)

    return HttpResponse(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def task_change_attributes(request, name):
    data = {}
    task_manager = TaskManager(request, name)

    if not task_manager.check_task_exists(name):
        return HttpResponse(data, status=HTTP_400_BAD_REQUEST)

    to_change_name = request.POST.get('to_change_name')
    to_change_description = request.POST.get('to_change_description')
    to_change_finish_time = request.POST.get('to_change_finish_time')
    to_change_state = request.POST.get('to_change_state')

    if to_change_description:
        data['description_changes'] = task_manager.change_description(to_change_description)

    if to_change_finish_time:
        data['finish_time_changes'] = task_manager.change_finish_time(to_change_finish_time)

    if to_change_state:
        data['state_changes'] = task_manager.change_state(to_change_state)

    if to_change_name:
        data['name_changes'] = task_manager.change_name(to_change_name)

    return HttpResponse(json.dumps(data), status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def show_tasks(request):
    filter = {}
    task_manager = TaskManager(request)
    for value in request.POST:
        filter[value] = request.POST.get(value)
    data = task_manager.show_tasks(filter)
    return HttpResponse(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def show_history(request, name):
    task_manager = TaskManager(request, name)

    if not task_manager.check_task_exists(name):
        return HttpResponse({}, status=HTTP_400_BAD_REQUEST)

    data = task_manager.show_history()
    return HttpResponse(data, status=HTTP_200_OK)
