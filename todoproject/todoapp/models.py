from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class TodoList(models.Model):
    title = models.CharField(max_length=100)

class TodoListItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    todo_list = models.ForeignKey(TodoList, related_name='items', on_delete=models.CASCADE)






'''def get_default_todo_list():
    """ get a default value for todo_list; create new todo_list if not available """
    return TodoList.objects.get_or_create(id=0, title='created')[0]

def get_default_todo_list_id():
    return get_default_todo_list().id
   ''' 