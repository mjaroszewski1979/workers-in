from django.shortcuts import render, get_object_or_404
from . models import Worker
from .forms import WorkerForm
from . import utilities 
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
import importlib

# import generic UpdateView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

class WorkersList(ListView):
    model = Worker
    template_name = 'index.html'

class WorkerCreateView(SuccessMessageMixin, CreateView):
    model = Worker
    template_name = 'worker_create.html'
    fields = '__all__'
    success_url = '.'
    success_message = "Worker was created successfully"

class WorkerUpdate(SuccessMessageMixin, UpdateView):
    model = Worker
    template_name = 'worker_update.html'
    fields = '__all__'
    success_url = '.'
    success_message = "Worker was updated successfully"

class WorkerDetail(DetailView):
    model = Worker
    template_name = 'worker_detail.html'

class WorkerDelete(SuccessMessageMixin, DeleteView):
    model = Worker
    template_name = 'worker_delete.html'
    success_url ="/"
    success_message = "Worker was deleted successfully"

class ProfsView(View):
    
    def get(self, request):
        context = {}
        importlib.reload(utilities)
        context['profs'] = utilities.score
        return render(request, 'profs.html', context)

