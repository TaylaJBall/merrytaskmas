from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import TodoList

# Create your views here.
class TodoList(ListView):
    model = TodoList
    template_name = 'task/todo_list.html'
    context_object_name = 'tasks'
    
    