from django.shortcuts import render, get_object_or_404
from . models import Worker
from . import utilities 
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
import importlib
from django.views.generic import View
from django.http import JsonResponse

import csv

from django.http import HttpResponse


# import generic UpdateView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

class WorkersList(ListView):
    paginate_by = 5
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
    success_url = '/'
    success_message = "Worker was updated successfully"

class WorkerDetail(DetailView):
    model = Worker
    template_name = 'worker_detail.html'


class AverageView(View):
    
    def get(self, request):
        context = {}
        importlib.reload(utilities)
        context['average'] = utilities.score
        return render(request, 'average.html', context)

class DeleteWorker(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Worker.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Profession', 'Average age'])

    data = utilities.score
    writer.writerow(data)

    response['Content-Disposition'] = 'attachment; filename="average.csv"'

    return response



