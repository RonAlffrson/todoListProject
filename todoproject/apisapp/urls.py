from django.urls import path

from .views import TodoListItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoListItemViewSet, basename='todos')
urlpatterns = router.urls
