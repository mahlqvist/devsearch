from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse("<h1>Hello world</h1>\n<h3>Here are my projects</h3>")
