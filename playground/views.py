from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoModel


def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'World'})
    #return HttpResponse(f'Hello, World! {x} + {y} = {x + y}')

def todos(request):
    return render(request, 'todos.html', {'todos': TodoModel.objects.all()})