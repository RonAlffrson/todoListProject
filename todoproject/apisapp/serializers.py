# apis/serializers.py
from rest_framework import serializers
from todoapp import models


class TodoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'created_date',
            'due_date'
        )
        model = models.TodoListItem