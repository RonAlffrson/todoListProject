from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class TodoListItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
