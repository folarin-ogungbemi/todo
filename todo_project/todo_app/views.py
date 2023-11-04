from django.shortcuts import render

# Create your views here.


def todo_list(request):
    # todo code here
    return render(request, 'todo_app/todo_list.html')
