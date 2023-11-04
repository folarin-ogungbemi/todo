from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo_app/todo_list.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todo_app/add_todo.html', context)
