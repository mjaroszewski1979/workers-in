import csv

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin



from . models import Worker


# import generic UpdateView


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
        context['average'] = Worker.objects.get_average_age()
        return render(request, 'average.html', context)

class CsvView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Profession', 'Average age'])
        data = Worker.objects.get_average_age()
        for obj in data:
            writer.writerow(obj)
        response['Content-Disposition'] = 'attachment; filename="average.csv"'
        return response







