from .views import TodoListItemViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register('', TodoListItemViewSet, basename='todos')
router.register(r'users', UserViewSet, basename='user' )


urlpatterns = router.urls

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]