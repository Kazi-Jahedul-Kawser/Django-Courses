from django.urls import path
from task.views import add_task, edit_task, delete_task

urlpatterns = [
    path('add/', add_task, name='task'),
    path('edit/<int:id>', edit_task, name='edit'),
    path('delete/<int:id>', delete_task, name='delete')
]

