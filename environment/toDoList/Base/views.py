from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

class TaskList(ListView):
    model=Task     
    context_object_name="Tasks"

class DetailTask(DetailView):
    model=Task
    context_object_name="Detail"