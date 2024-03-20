from django.shortcuts import render
from .models import TodoListItem, TodoList
from django.http import HttpResponseRedirect 
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    all_todo_lists = TodoList.objects.all()
    if all_todo_lists.query.is_empty:
        print(all_todo_lists)
    return render(request, 'index.html', {'all_items': all_todo_items, 'all_lists' : all_todo_lists})

@login_required(redirect_field_name=' ') #user is redirected to index page without creating a todo item
def addTodoListView(request):
    x = request.POST['title']
    request.user

    new_item = TodoList(title = x)
    new_item.save()
    return HttpResponseRedirect('/') 


@login_required(redirect_field_name=' ')
def deleteTodoList(request, i):
    item = TodoList.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/') 

@login_required(redirect_field_name=' ')
def deleteAllTodoListsView(request):
    all_items = TodoList.objects.all()
    all_items.delete()

    return HttpResponseRedirect('/')

@login_required(redirect_field_name=' ') #user is redirected to index page without creating a todo item
def addTodoView(request):
    x = request.POST['title']
    y = request.POST['description']
    z = request.POST['due_date']
    request.user

    new_item = TodoListItem(title = x, description = y, created_date = timezone.now, due_date = z, owner=request.user)
    new_item.save()
    return HttpResponseRedirect('/') 

@login_required(redirect_field_name=' ')
def deleteTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/') 

@login_required(redirect_field_name=' ')
def deleteAllTodoView(request):
    all_items = TodoListItem.objects.all()
    all_items.delete()

    return HttpResponseRedirect('/')

@login_required(redirect_field_name=' ')
def renameItemTitleView(request, i):
    new_title = request.POST['title']
    item = TodoListItem.objects.get(id=i)

    item.title = new_title
    item.save()
    return HttpResponseRedirect('/')

@login_required(redirect_field_name=' ')
def renamePageView(request, i):
    return render(request, 'rename.html', {'i' : TodoListItem.objects.get(id=i)})

@login_required(redirect_field_name=' ')
def changeDescriptionPageView(request, i):
    return render(request, 'changeDescription.html', {'i' : TodoListItem.objects.get(id=i)})

@login_required(redirect_field_name=' ')
def changeItemDescriptionView(request, i):
    new_desc = request.POST['description']
    item = TodoListItem.objects.get(id=i)

    item.description = new_desc
    item.save()
    return HttpResponseRedirect('/')

@login_required(redirect_field_name=' ')
def changeDatePageView(request, i):
    return render(request, 'changeDate.html', {'i' : TodoListItem.objects.get(id=i)})

@login_required(redirect_field_name=' ')
def changeDateView(request, i):
    new_date = request.POST['due_date']
    item = TodoListItem.objects.get(id=i)

    item.due_date = new_date
    item.save()
    return HttpResponseRedirect('/')