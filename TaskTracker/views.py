#TaskTracker/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm

def home(request):
    return render(request, 'home.html')
def mark_complete(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed  # Toggle completed status
    task.save()
    return redirect('task_list')


def task_list(request):
    # Categorize tasks based on the `category` field
    do_now = Task.objects.filter(category='urgent_important')
    schedule = Task.objects.filter(category='not_urgent_important')
    delegate = Task.objects.filter(category='urgent_not_important')
    limit = Task.objects.filter(category='not_urgent_not_important')

    context = {
        'do_now': do_now,
        'schedule': schedule,
        'delegate': delegate,
        'limit': limit,
    }
    return render(request, 'TaskTracker/task_list.html', context)


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'TaskTracker/task_detail.html', {'task': task})


def task_add(request):
    if request.method == 'POST':  # When form is submitted
        print("POST request received")  # Debugging statement
        form = TaskForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging statement
            form.save()
            return redirect('task_list')
        else:
            print("Form is invalid")  # Debugging statement
            print(form.errors)  # Print form errors for debugging
    else:  # When the page is loaded
        form = TaskForm()
    return render(request, 'TaskTracker/task_add.html', {'form': form})


def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'TaskTracker/task_edit.html', {'form': form})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')
