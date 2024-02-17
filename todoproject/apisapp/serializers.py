# apis/serializers.py
from rest_framework import serializers
from todoapp.models import TodoListItem 
from django.contrib.auth.models import User


class TodoListItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'created_date',
            'due_date',
            'owner'
        )
        model = TodoListItem

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=TodoListItem.objects.all())
    class Meta:
        fields = (
            'id', 
            'username'
            'todos'
        )
        model = User