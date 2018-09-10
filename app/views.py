from django.http import HttpResponse
from django.shortcuts import render

from .models import TestObject

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def db(request):

    greeting = TestObject()
    greeting.save()

    greetings = TestObject.objects.all()

    return render(request, 'db.html', {'greetings': greetings})    