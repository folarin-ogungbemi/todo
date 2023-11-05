from django.shortcuts import (
    render, redirect, get_object_or_404)
from .models import Todo
from .forms import TodoForm

# Create your views here.


def add_todo(request):
    # CREATE a todo item
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


def todo_list(request):
    # READ a list of todo items
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo_app/todo_list.html', context)


def edit_todo(request, todo_id):
    # UPDATE a todo item
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        form.save()
        return redirect('todos')
    form = TodoForm(instance=todo)
    context = {
        'form': form
    }
    return render(request, 'todo_app/update_todo.html', context)


def delete_todo(request, todo_id):
    # DELETE a todo item
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todos')