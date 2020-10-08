from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

from rest_framework.authtoken import views
from .views import register

urlpatterns = [
    path('tasks', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('login', views.obtain_auth_token),
    path('register', register)
]
