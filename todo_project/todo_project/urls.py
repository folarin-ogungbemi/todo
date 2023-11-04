from django.contrib import admin
from django.urls import path
from todo_app.views import todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', todo_list,)
]
