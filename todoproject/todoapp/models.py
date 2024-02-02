from django.db import models

# Create your models here.
from django.db import models
class TodoListItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
