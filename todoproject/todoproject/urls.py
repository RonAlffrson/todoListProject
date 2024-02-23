"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todoapp.views import todoappView, addTodoView, deleteTodoView, deleteAllTodoView, renameItemTitleView
from todoapp.views import renamePageView, changeDescriptionPageView, changeItemDescriptionView
from todoapp.views import changeDatePageView, changeDateView 



urlpatterns = [
    path('admin/', admin.site.urls),
    #todoapp
    #path('todoapp/', todoappView),
    path('', todoappView),#TODO: change this mess
    path('addTodoItem/', addTodoView), 
    path('deleteTodoItem/<int:i>/', deleteTodoView), 
    path('deleteAllTodoItems/', deleteAllTodoView),
    path('renameItemTitle/<int:i>/', renameItemTitleView),
    path('renamePage/<int:i>/', renamePageView),
    path('changeDescriptionPage/<int:i>/', changeDescriptionPageView),
    path('changeDescription/<int:i>/', changeItemDescriptionView),
    path('changeDatePage/<int:i>/', changeDatePageView),
    path('changeDate/<int:i>/', changeDateView),
    path('accounts/', include('django.contrib.auth.urls')),
    #apisapp
    path('apisapp/v1/', include('apisapp.urls'))
]
