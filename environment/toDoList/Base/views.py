from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

class TaskList(LoginRequiredMixin,ListView):
    model=Task     
    context_object_name="Tasks"

    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        context['Tasks']=context['Tasks'].filter(user=self.request.user)
        context['Count']=context['Tasks'].filter(complete=False).count()

        searchInput=self.request.GET.get('Serching') or ''
        if searchInput:
            context['Tasks']=context['Tasks'].filter(title__startswith=searchInput)
        
        context['searchInput']=searchInput

        return context

class DetailTask(LoginRequiredMixin,DetailView):
    model=Task
    context_object_name="Detail"

class TaskCreate(LoginRequiredMixin,CreateView):
    model= Task
    fields=['title','description','complete']
    success_url=reverse_lazy('Tasks')

    def form_valid(self, form): 
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)
        

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('Tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name="Tasks"
    success_url=reverse_lazy('Tasks')

class LoginV(LoginView):
    template_name='Base/login.html'
    field='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('Tasks')

class RegisterP(FormView):
    template_name="Base/register.html"
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('Tasks')

    def form_valid(self, form):
        user=form.save()
        if user:
            login(self.request,user)
        return super(RegisterP,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('Tasks')
        return super(RegisterP,self).get(*args,**kwargs)

