from django.shortcuts import render
from django.http import HttpResponse
from main.models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
