from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http import HttpResponse


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


#TODO:другие статусы
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username):
            User.objects.create_user(username=username, password=password)
            return HttpResponse(status=HTTP_200_OK)

    return HttpResponse(status=HTTP_400_BAD_REQUEST)
