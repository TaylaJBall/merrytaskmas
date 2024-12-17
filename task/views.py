from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView, FormView
from django.urls import reverse_lazy

from .models import TodoList
from .models import Task

# Create your views here.
class TodoList(ListView):
    model = TodoList
    template_name = 'task/todo_list.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task/task.html'
    context_object_name = 'task'

class TodoCreate(CreateView):
    model = Task
    fields = ['description', 'is_completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)


class TodoUpdate(UpdateView):
    model = Task
    fields = ['description', 'is_completed']
    success_url = reverse_lazy('tasks')


class DeleteTodo(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')    
    

    
    