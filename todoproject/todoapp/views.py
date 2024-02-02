from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect 


# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'index.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['name']
    y = request.POST['description']

    new_item = TodoListItem(name = x, description = y)
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 

def deleteTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/todoapp/') 

def deleteAllTodoView(request):
    all_items = TodoListItem.objects.all()
    all_items.delete()

    return HttpResponseRedirect('/todoapp/')

'''def renameTodoView(request, i):
    new_name = request.POST['description']
    item = TodoListItem.objects.get(id=i)
'''