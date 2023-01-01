from datetime import date

from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from my_finances.forms import IncomeForm, OutcomeForm, BalanceForm
from . import models
from my_finances.helpers import calculate_repetitive_total

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
    template_name = 'my_finances/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return models.Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Balance deleted successfully!')
        return reverse_lazy('my_finances:balance_list')


def current_period(request):
    today = date.today()
    last_balance = models.Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
    if not last_balance:
        messages.warning(request, 'No current balance has been recorded. '
                                  'Please add at least one current balance record.')
        return render(request, 'my_finances/current_period.html')

        # initialise totals with sums of non repetitive incomes and outcomes
    total_income = models.Income.objects \
        .filter(user=request.user, date__gt=last_balance.date, date__lte=today, repetitive=False) \
        .aggregate(total=Sum('value'))['total']
    total_income = 0 if total_income is None else total_income
    total_outcome = models.Outcome.objects \
        .filter(user=request.user, date__gt=last_balance.date, date__lte=today, repetitive=False) \
        .aggregate(total=Sum('value'))['total']
    total_outcome = 0 if total_outcome is None else total_outcome

    # updated totals with repetitive
    for income in models.Income.objects.filter(user=request.user, repetitive=True):
        total_income += calculate_repetitive_total(income, last_balance.date, today)
    for outcome in models.Outcome.objects.filter(user=request.user, repetitive=True):
        total_outcome += calculate_repetitive_total(outcome, last_balance.date, today)
    context = {
        'balance': last_balance
    }
    return render(request, 'my_finances/current_period.html', context=context)


def year_overview(request):
    return render(request, template_name='my_finances/year_overview.html')
