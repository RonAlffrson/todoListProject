from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect 
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})

@login_required(redirect_field_name=' ') #user is redirected to index page without creating a todo item
def addTodoView(request):
    x = request.POST['title']
    y = request.POST['description']
    z = request.POST['due_date']
    request.user

    new_item = TodoListItem(title = x, description = y, created_date = timezone.now, due_date = z, owner=request.user)
    new_item.save()
    return HttpResponseRedirect('/') 

def deleteTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/') 

def deleteAllTodoView(request):
    all_items = TodoListItem.objects.all()
    all_items.delete()

    return HttpResponseRedirect('/')

def renameItemTitleView(request, i):
    new_title = request.POST['title']
    item = TodoListItem.objects.get(id=i)

    item.title = new_title
    item.save()
    return HttpResponseRedirect('/')

def renamePageView(request, i):
    return render(request, 'rename.html', {'i' : TodoListItem.objects.get(id=i)})

def changeDescriptionPageView(request, i):
    return render(request, 'changeDescription.html', {'i' : TodoListItem.objects.get(id=i)})

def changeItemDescriptionView(request, i):
    new_desc = request.POST['description']
    item = TodoListItem.objects.get(id=i)

    item.description = new_desc
    item.save()
    return HttpResponseRedirect('/')

def changeDatePageView(request, i):
    return render(request, 'changeDate.html', {'i' : TodoListItem.objects.get(id=i)})

def changeDateView(request, i):
    new_date = request.POST['due_date']
    item = TodoListItem.objects.get(id=i)

    item.due_date = new_date
    item.save()
    return HttpResponseRedirect('/')