from django.urls import path

from . import views

urlpatterns = [
    path('/home', views.home, name='home'),
    path('/create', views.task_create, name='create'),
    path('/change/<str:name>', views.task_change_attributes, name='change_attr'),
    path('/show', views.show_tasks, name='show_tasks'),
    path('/show_history/<str:name>', views.show_history, name='show_history')
]