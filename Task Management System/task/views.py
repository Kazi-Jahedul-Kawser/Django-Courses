from django.shortcuts import render, redirect
from task.forms import Add_Task
from task.models import Task
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        add_task =  Add_Task(request.POST)
        if add_task.is_valid():
            add_task.save()
            return redirect('home')
    else:
        add_task = Add_Task()
        
    return render(request,'task.html', {'task':add_task})

def edit_task(request, id):
    task_instance = Task.objects.get(pk=id)
    if request.method =='POST':
        edit_task = Add_Task(request.POST, instance=task_instance)
        if edit_task.is_valid():
            edit_task.save()
            return redirect('home')
    else:
        edit_task = Add_Task(instance=task_instance)
        
    return render(request,'task.html', {'task':edit_task})
    

def delete_task(request, id):
    task_instance = Task.objects.get(pk=id)
    task_instance.delete()
    return redirect('home')

