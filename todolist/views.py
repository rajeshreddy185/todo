from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Todo


# Create your views here.
def create(request):
    if request.method == 'POST':
        t = Todo.objects.create(title=request.POST['title'])
        t.save()
        return HttpResponseRedirect('/todolist/')

    return render(request, 'todolist/create.html')


def home(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/home.html', {'todos': todos})


def delete(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect('/todolist/')
