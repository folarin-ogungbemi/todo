from django.contrib import admin
from django.urls import path
from todo_app.views import todo_list, create_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todos'),
    path('add', create_todo, name='add_todo'),
]
