from django.urls import path
from .views import TaskList,DetailTask

urlpatterns=[
    path('',TaskList.as_view(),name='Tasks'),
    path('task/<int:pk>/',DetailTask.as_view(),name='Detail'),

]