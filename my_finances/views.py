from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from my_finances.forms import IncomeForm
from . import models


# Create your views here.
class IncomeListVIew(ListView):
    model = models.Income
    paginate_by = 100


class IncomeDetailView(DetailView):
    model = models.Income


class IncomeCreateView(CreateView):
    model = models.Income
    form_class = IncomeForm

    def get_success_url(self):
        messages.success(self.request, 'Income created successfully')
        return reverse_lazy('my_finances:income_list')


class IncomeUpdateView(UpdateView):
    model = models.Income
    form_class = IncomeForm

    def get_success_url(self):
        messages.success(self.request, 'Income updated successfully')
        return reverse('my_finances:income_detail', kwargs={'pk': self.object.pk})


class IncomeDeleteView(DeleteView):
    model = models.Income

    def get_success_url(self):
        messages.success(self.request, 'Income deleted successfully')
        return reverse_lazy('my_finances:income_list')
