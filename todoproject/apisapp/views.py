from rest_framework import generics, viewsets

from todoapp import models
from .serializers import TodoListItemSerializer

'''class ListTodo(generics.ListCreateAPIView):
    queryset = models.TodoListItem.objects.all()
    serializer_class = TodoListItemSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TodoListItem.objects.all()
    serializer_class = TodoListItemSerializer
'''
class TodoListItemViewSet(viewsets.ModelViewSet):
    queryset = models.TodoListItem.objects.all()
    serializer_class = TodoListItemSerializer