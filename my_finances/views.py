from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from my_finances.forms import IncomeForm, OutcomeForm, BalanceForm
from . import models


# Views for the Income
class IncomeListVIew(ListView):
    model = models.Income
    paginate_by = 100
    template_name = 'my_finances/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return models.Income.objects.filter(user=user)


class IncomeDetailView(DetailView):
    model = models.Income
    template_name = 'my_finances/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return models.Income.objects.filter(user=user)


class IncomeCreateView(CreateView):
    model = models.Income
    form_class = IncomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Income'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Income created successfully')
        return reverse_lazy('my_finances:income_list')


class IncomeUpdateView(UpdateView):
    model = models.Income
    form_class = IncomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Income'}

    def get_queryset(self):
        user = self.request.user
        return models.Income.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Income updated successfully')
        return reverse('my_finances:income_detail', kwargs={'pk': self.object.pk})


class IncomeDeleteView(DeleteView):
    model = models.Income
    template_name = 'my_finances/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return models.Income.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Income deleted successfully')
        return reverse_lazy('my_finances:income_list')

# Views for the Outcome
class OutcomeListVIew(ListView):
    model = models.Outcome
    paginate_by = 100
    template_name = 'my_finances/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return models.Outcome.objects.filter(user=user)


class OutcomeDetailView(DetailView):
    model = models.Outcome
    template_name = 'my_finances/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return models.Outcome.objects.filter(user=user)


class OutcomeCreateView(CreateView):
    model = models.Outcome
    form_class = OutcomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Outcome'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Outcome created successfully')
        return reverse_lazy('my_finances:outcome_list')


class OutcomeUpdateView(UpdateView):
    model = models.Outcome
    form_class = OutcomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Outcome'}

    def get_queryset(self):
        user = self.request.user
        return models.Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome updated successfully')
        return reverse('my_finances:outcome_detail', kwargs={'pk': self.object.pk})


class OutcomeDeleteView(DeleteView):
    model = models.Outcome
    template_name = 'my_finances/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return models.Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome deleted successfully')
        return reverse_lazy('my_finances:outcome_list')

# Views for the balances
class BalanceListView(ListView):
    model = models.Balance
    paginate_by = 100
    template_name = 'my_finances/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return models.Balance.objects.filter(user=user)


class BalanceDetailView(DetailView):
    model = models.Balance
    template_name = 'my_finances/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return models.Balance.objects.filter(user=user)


class BalanceCreatView(CreateView):
    model = models.Balance
    form_class = BalanceForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Balance'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Balance created successfully!')
        return reverse_lazy('my_finances:balance_list')


class BalanceUpdateView(UpdateView):
    model = models.Balance
    form_class = BalanceForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Balance'}

    def get_queryset(self):
        user = self.request.user
        return models.Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Balance updated successfully!')
        return reverse('my_finances:balance_detail', kwargs={'pk': self.object.pk})


class BalanceDeleteView(DeleteView):
    model = models.Balance
    template_name = 'my_finances/models.Balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'models.Balance'}

    def get_queryset(self):
        user = self.request.user
        return models.Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'models.Balance deleted successfully!')
        return reverse_lazy('my_finances:balance_list')
