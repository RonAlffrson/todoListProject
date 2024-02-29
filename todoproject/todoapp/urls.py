from django.urls import path
from todoapp.views import todoappView, addTodoView, deleteTodoView, deleteAllTodoView, renameItemTitleView
from todoapp.views import renamePageView, changeDescriptionPageView, changeItemDescriptionView
from todoapp.views import changeDatePageView, changeDateView 

urlpatterns =  [
    path('', todoappView),
    path('addTodoItem/', addTodoView), 
    path('deleteTodoItem/<int:i>/', deleteTodoView), 
    path('deleteAllTodoItems/', deleteAllTodoView),
    path('renameItemTitle/<int:i>/', renameItemTitleView),
    path('renamePage/<int:i>/', renamePageView),
    path('changeDescriptionPage/<int:i>/', changeDescriptionPageView),
    path('changeDescription/<int:i>/', changeItemDescriptionView),
    path('changeDatePage/<int:i>/', changeDatePageView),
    path('changeDate/<int:i>/', changeDateView),
]