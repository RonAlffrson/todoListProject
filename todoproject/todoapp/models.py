from django.db import models

# Create your models here.
from django.db import models
class TodoListItem(models.Model):
    name = models.CharField()
    description = models.TextField() 
