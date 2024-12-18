from django.urls import path
from .views import TodoListView, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TodoListView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name="task-create"),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]