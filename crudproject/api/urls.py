from django.urls import path
from .views import get_tasks, create_task, task_detail, smart_task_suggestions

urlpatterns = [
    path('tasks/', get_tasks, name='get_tasks'),
    path('tasks/create', create_task, name = 'create_task'),
    path('tasks/<int:pk>', task_detail, name = 'task_detail'),
    path('smart-suggestions/', smart_task_suggestions, name='smart_task_suggestions')
]