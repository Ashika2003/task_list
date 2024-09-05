from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()

    # Filtering by status
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # Sorting
    sort_by = request.GET.get('sort_by')
    if sort_by in ['priority', 'due_date']:
        tasks = tasks.order_by(sort_by)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})
