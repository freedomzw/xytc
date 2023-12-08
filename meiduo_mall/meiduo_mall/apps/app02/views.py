from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse(reverse('app02:index'))
