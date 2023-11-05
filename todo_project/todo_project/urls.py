from django.contrib import admin
from django.urls import path
from todo_app.views import (
    todo_list, add_todo,
    edit_todo, delete_todo,
    toggle_status)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todos'),
    path('add', add_todo, name='add_todo'),
    path('edit/<todo_id>', edit_todo, name='edit'),
    path('delete/<todo_id>', delete_todo, name='delete'),
    path('toggle/<todo_id>', toggle_status, name='toggle'),
]
