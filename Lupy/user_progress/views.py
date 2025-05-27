from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello, user!</h1>')

def add_abilities(request):
    return HttpResponse('<h1>Add abilities here</h1>')


