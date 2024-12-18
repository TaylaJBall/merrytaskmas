from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TodoList, Task

class TodoListView(LoginRequiredMixin, ListView):
    model = Task  # We want to list tasks, not TodoLists
    template_name = 'task/todo_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        """Filter tasks that belong to the user's specific TodoList."""
        todo_list, created = TodoList.objects.get_or_create(user=self.request.user, defaults={'title': 'My Default TodoList'})
        return todo_list.task_set.all()  # Get all tasks associated with this TodoList
       

    def get_context_data(self, **kwargs):
        """Add count of incomplete tasks to the context."""
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().filter(is_completed=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/todo_list.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['description', 'is_completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        """Attach the task to the correct TodoList for this user."""
        todo_list = TodoList.objects.filter(user=self.request.user).first()
        if todo_list:  # Make sure the TodoList exists
            form.instance.todo_list = todo_list
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['description', 'is_completed']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/todo_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')