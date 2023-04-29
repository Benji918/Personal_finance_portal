from datetime import date, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from my_finances.forms import IncomeForm, OutcomeForm, BalanceForm
from my_finances.helpers import calculate_repetitive_total
from my_finances.models import Income, Outcome, Balance


@method_decorator(login_required, name='dispatch')
class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    template_name = 'my_finances/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class IncomeDetailView(DetailView):
    model = Income
    template_name = 'my_finances/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Income'}

    # queryset = Income.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income'


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Income'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Income created successfully!')
        return reverse_lazy('my_finances:income_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Income'}

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Income updated successfully!')
        return reverse('my_finances:income_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'my_finances/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Income'}

    # template_name_suffix = '_delete_form'
    # queryset = Income.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)

    # context_object_name = 'income'

    def get_success_url(self):
        messages.success(self.request, 'Income deleted successfully!')
        return reverse_lazy('my_finances:income_list')


class OutcomeListView(ListView):
    model = Outcome
    paginate_by = 100
    template_name = 'my_finances/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'my_finances/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=user)


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class OutcomeCreateView(CreateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Outcome'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Outcome created successfully!')
        return reverse_lazy('my_finances:outcome_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class OutcomeUpdateView(UpdateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome updated successfully!')
        return reverse('my_finances:outcome_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class OutcomeDeleteView(DeleteView):
    model = Outcome
    template_name = 'my_finances/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome deleted successfully!')
        return reverse_lazy('my_finances:outcome_list')


@method_decorator(login_required, name='dispatch')
class BalanceListView(ListView):
    model = Balance
    paginate_by = 100
    template_name = 'my_finances/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class BalanceDetailView(DetailView):
    model = Balance
    template_name = 'my_finances/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class BalanceCreateView(CreateView):
    model = Balance
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


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class BalanceUpdateView(UpdateView):
    model = Balance
    form_class = BalanceForm
    template_name = 'my_finances/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Balance updated successfully!')
        return reverse_lazy('my_finances:balance_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class BalanceDeleteView(DeleteView):
    model = Balance
    template_name = 'my_finances/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Balance deleted successfully!')
        return reverse_lazy('my_finances:balance_list')


@login_required()
def current_period(request):
    make_calls = True
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
    if not last_balance:
        messages.warning(request, 'No current balance has been recorded. '
                                  'Please add at least one current balance record.')
        make_calls = False
    return render(request, 'my_finances/current_period.html', context={'make_calls': make_calls})


@login_required
def year_overview(request):
    make_calls = True
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
    last_savings_balance = Balance.objects.filter(user=request.user, type=2).order_by('-date').first()
    if last_balance is None and last_savings_balance is None:
        messages.warning(request, 'No current balance has been recorded. '
                                  'Please add at least one current balance record.')
        make_calls = False
    return render(request, 'my_finances/year_overview.html', context={'make_calls': make_calls})


@login_required
def get_summary_tiles(request):
    today = date.today()
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
    if not last_balance:
        return JsonResponse({'error': 'No current balance has been recorded. '
                                      'Please add at least one current balance record.'})
    # initialise totals with sums of non-repetitive incomes and outcomes
    total_income = Income.objects \
        .filter(user=request.user, date__gt=last_balance.date, date__lte=today, repetitive=False) \
        .aggregate(total=Sum('value'))['total']
    print(total_income)
    total_income = 0 if total_income is None else total_income
    total_outcome = Outcome.objects \
        .filter(user=request.user, date__gt=last_balance.date, date__lte=today, repetitive=False) \
        .aggregate(total=Sum('value'))['total']
    total_outcome = 0 if total_outcome is None else total_outcome

    # updated totals with repetitive
    for income in Income.objects.filter(user=request.user, repetitive=True):
        total_income += calculate_repetitive_total(income, last_balance.date, today)
    for outcome in Outcome.objects.filter(user=request.user, repetitive=True):
        total_outcome += calculate_repetitive_total(outcome, last_balance.date, today)
        print(total_outcome)
    return JsonResponse({
        'last_balance_value': last_balance.value,
        'last_balance_date': last_balance.date,
        'estimated_balance': last_balance.value + total_income - total_outcome,
        'total_income': total_income,
        'total_outcome': total_outcome
    })


@login_required
def get_year_chart(request):
    balance_type = request.GET.get('balance_type')
    if balance_type not in ['current', 'savings']:
        return JsonResponse({'error', 'Please specify balance_type parameter to be either "current" or "savings".'})

    today = date.today()
    beginning_of_year = date(today.year, 1, 1)
    end_of_year = date(today.year, 12, 28)
    # Try to get last balance check before the beginning of this year
    balance = Balance.objects.filter(user=request.user, type=1 if balance_type == 'current' else 2,
                                     date__lte=beginning_of_year).order_by('-date').first()
    if balance is None:
        # If there's no balance check before the year - get this first one of this year
        balance = Balance.objects.filter(user=request.user, type=1 if balance_type == 'current' else 2) \
            .order_by('date').first()
        if balance is None:
            return JsonResponse({'error': 'No current balance has been recorded. '
                                          'Please add at least one current balance record.'})

    # Assuming we found balance - we start calculating from there
    balance_checks = {}
    income_per_day = {}
    outcome_per_day = {}

    for b in Balance.objects.filter(user=request.user, type=1 if balance_type == 'current' else 2,
                                    date__gte=balance.date):
        balance_checks[str(b.date)] = b.value

    if balance_type == 'current':
        for i in Income.objects.filter(user=request.user, date__gte=balance.date, repetitive=False):
            income_per_day[str(i.date)] = i.value if str(i.date) not in income_per_day \
                else income_per_day[str(i.date)] + i.value
        for o in Outcome.objects.filter(user=request.user, date__gte=balance.date, repetitive=False):
            outcome_per_day[str(o.date)] = o.value if str(o.date) not in outcome_per_day \
                else outcome_per_day[str(o.date)] + o.value

        for income in Income.objects.filter(user=request.user, repetitive=True):
            calculate_repetitive_total(income, balance.date, end_of_year, income_per_day)
        for outcome in Outcome.objects.filter(user=request.user, repetitive=True):
            calculate_repetitive_total(outcome, balance.date, end_of_year, outcome_per_day)
    else:
        # If balance_type is savings, we want to only look at incomes and outcomes of type SAVINGS
        # Also, income of type SAVINGS will act like an outcome for savings balance and vice versa
        for i in Income.objects.filter(user=request.user, date__gte=balance.date, type=5, repetitive=False):
            outcome_per_day[str(i.date)] = i.value if str(i.date) not in outcome_per_day \
                else outcome_per_day[str(i.date)] + i.value
        for o in Outcome.objects.filter(user=request.user, date__gte=balance.date, type=10, repetitive=False):
            income_per_day[str(o.date)] = o.value if str(o.date) not in income_per_day \
                else income_per_day[str(o.date)] + o.value

        for income in Income.objects.filter(user=request.user, type=5, repetitive=True):
            calculate_repetitive_total(income, balance.date, end_of_year, outcome_per_day)
        for outcome in Outcome.objects.filter(user=request.user, type=10, repetitive=True):
            calculate_repetitive_total(outcome, balance.date, end_of_year, income_per_day)

    labels = []
    data_estimated = []
    data_balance_check = []
    data_today = []
    date_marker = balance.date
    balance_on_marker_date = balance.value

    if date_marker > beginning_of_year:
        fill_date_marker = date(today.year, 1, 1)
        while fill_date_marker < date_marker:
            labels.append(str(fill_date_marker))
            data_estimated.append(None)
            data_balance_check.append(None)
            data_today.append(None)
            fill_date_marker += timedelta(days=1)
    else:
        while date_marker < beginning_of_year:
            balance_on_marker_date += income_per_day.get(str(date_marker), 0)
            balance_on_marker_date -= outcome_per_day.get(str(date_marker), 0)
            date_marker += timedelta(days=1)

    # Calculate and prepare balance per day for this year
    while date_marker <= end_of_year:
        labels.append(str(date_marker))
        if str(date_marker) in balance_checks:
            balance_on_marker_date = balance_checks[str(date_marker)]
            data_balance_check.append(balance_checks[str(date_marker)])
        else:
            balance_on_marker_date += income_per_day.get(str(date_marker), 0)
            balance_on_marker_date -= outcome_per_day.get(str(date_marker), 0)
            data_balance_check.append(None)
        data_estimated.append(balance_on_marker_date)
        if date_marker == today:
            data_today.append(balance_on_marker_date)
        else:
            data_today.append(None)
        date_marker += timedelta(days=1)
    return JsonResponse({'labels': labels, 'data_estimated': data_estimated, 'data_balance_check': data_balance_check,
                         'data_today': data_today})


@login_required()
def get_income_or_outcome_by_type(request):
    get_what = request.GET.get('get_what')
    summary_type = request.GET.get('summary_type')
    if get_what is None or get_what not in ['income', 'outcome']:
        return JsonResponse({'error': 'Please specify get_what parameter to be either "income" or "outcome".'})
    if get_what == 'income':
        obj = Income
        obj_types = Income.ITypes
    else:
        obj = Outcome
        obj_types = Outcome.OTypes

    today = date.today()
    if summary_type == 'current_period':
        last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
        if not last_balance:
            return JsonResponse({'error': 'No current balance has been recorded. '
                                          'Please add at least one current balance record.'})
        start_date = last_balance.date
        end_date = today
    elif summary_type == 'year_overview':
        start_date = date(today.year - 1, 12, 31)
        end_date = date(today.year, 12, 31)
    else:
        return JsonResponse({'error': 'Please specify summary_type parameter to be either "current_period" or '
                                      '"year_overview".'})

    labels = []
    data = []
    for obj_type in obj_types.choices:
        labels.append(obj_type[1])
        total = obj.objects.filter(user=request.user, type=obj_type[0], date__gt=start_date,
                                   date__lte=end_date, repetitive=False).aggregate(total=Sum('value'))['total']
        total = 0 if total is None else total

        for o in obj.objects.filter(user=request.user, type=obj_type[0], repetitive=True):
            total += calculate_repetitive_total(o, start_date, end_date)
        data.append(total)

    return JsonResponse({'labels': labels, 'data': data})
