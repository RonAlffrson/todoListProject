from rest_framework import viewsets, permissions

from todoapp import models
from .serializers import TodoListItemSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


class TodoListItemViewSet(viewsets.ModelViewSet):
    queryset = models.TodoListItem.objects.all()
    serializer_class = TodoListItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        """The create() method of our serializer will now be passed an additional 'owner' field, 
        along with the validated data from the request."""

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer