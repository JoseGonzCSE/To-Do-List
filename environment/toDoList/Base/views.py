from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task

class TaskList(ListView):
    model=Task     
    context_object_name="Tasks"

class DetailTask(DetailView):
    model=Task
    context_object_name="Detail"

class TaskCreate(CreateView):
    model= Task
    fields='__all__'
    success_url=reverse_lazy('Tasks')

class TaskUpdate(UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('Tasks')

class TaskDelete(DeleteView):
    model=Task
    context_object_name="Tasks"
    success_url=reverse_lazy('Tasks')

class LoginV(LoginView):
    template_name='Base/login.html'
    field='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('Tasks')