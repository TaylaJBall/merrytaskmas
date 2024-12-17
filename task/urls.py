from django.urls import path
from .views import TodoList, TaskDetail, TodoCreate, TodoUpdate, DeleteTodo

urlpatterns = [
    path('', TodoList.as_view(), name='tasks'),
    # path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-todo/', TodoCreate.as_view(), name="task-create"),
    path('update-todo/<int:pk>/', TodoUpdate.as_view(), name='task-update'),
    path('delete-todo/<int:pk>/', DeleteTodo.as_view(), name='task-delete'),
]