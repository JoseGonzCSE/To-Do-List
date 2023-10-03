from django.urls import path
from .views import TaskList,DetailTask,TaskCreate,TaskUpdate,TaskDelete,LoginV
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',LoginV.as_view(),name='Login'),
    path('logout/',LogoutView.as_view(next_page='Login'),name='Logout'),
    path('',TaskList.as_view(),name='Tasks'),
    path('task/<int:pk>/',DetailTask.as_view(),name='Detail'),
    path('create-Task/',TaskCreate.as_view(),name='Create'),
    path('task-Update/<int:pk>/',TaskUpdate.as_view(),name='Update'),
    path('task-Delete/<int:pk>/',TaskDelete.as_view(),name='Delete'),
]