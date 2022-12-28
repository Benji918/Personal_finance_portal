from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from . import models

# Create your views here.
class IncomeListVIew(ListView):
    model = models.Income
    paginate_by = 100

class IncomeDetailView(DetailView):
    model = models.Income


class IncomeCreateView(CreateView):
    model = models.Income
    fields = [
        'value',
        'date',
        'type',
        'repetitive',
        'repetition_interval',
        'repetition_time',
        'repetition_end',
    ]
    success_url = reverse_lazy('my_finances:income_list')

class IncomeUpdateView(UpdateView):
    model = models.Income
    fields = [
        'value',
        'date',
        'type',
        'repetitive',
        'repetition_interval',
        'repetition_time',
        'repetition_end',
    ]
    success_url = reverse_lazy('my_finances:income_list')

class IncomeDeleteView(DeleteView):
    model = models.Income
    success_url = reverse_lazy('my_finances:income_list')