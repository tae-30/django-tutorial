from django.http import HttpResponse
from .models import Event
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


def schedule(request):
    return render(request, "apps/index.html")
