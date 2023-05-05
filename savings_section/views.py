from django.shortcuts import render

# Create your views here.
import datetime
import json

from django.contrib import messages
from django.db.models import Count, Sum, Prefetch
from django.db.models.functions import Trunc
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import SavingsAccount, Deposit, Withdrawal, SavingsGoal
from .forms import SavingsGoalForm, WithdrawalForm, DepositForm, SavingsAccountForm


# Create your views here.

@method_decorator(login_required, name='dispatch')
class SavingsAccountListView(ListView):
    model = SavingsAccount
    template_name = 'savings_section/savings_section_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'Savings'}

    def get_queryset(self):
        user = self.request.user
        return SavingsAccount.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsAccountCreateView(CreateView):
    model = SavingsAccount
    form_class = SavingsAccountForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Add Savings'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Savings user created successfully!')
        return reverse_lazy('savings_section:savings_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsAccountUpdateView(UpdateView):
    model = SavingsAccount
    form_class = SavingsAccountForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Update Savings'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Savings user updated successfully!')
        return reverse_lazy('savings_section:savings_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsAccountDetailView(DetailView):
    model = SavingsAccount
    template_name = 'savings_section/savings_section_detail.html'
    extra_context = {'detail_what': 'Savings'}

    def get_queryset(self):
        user = self.request.user
        return SavingsAccount.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsAccountDeleteView(DeleteView):
    model = SavingsAccount
    template_name = 'savings_section/savings_section_delete.html'
    extra_context = {'delete_what': 'Savings'}

    def get_queryset(self):
        user = self.request.user
        return SavingsAccount.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Savings user deleted successfully!')
        return reverse_lazy('savings_section:savings_list')


@method_decorator(login_required, name='dispatch')
class SavingsAccountSummaryTiles(TemplateView):
    template_name = 'savings_section/current_period.html'
    extra_context = {'display_what': 'Savings'}
    context_object_name = 'savings_data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        # Get the savings slug from the URL parameters
        savings_slug = self.kwargs['slug']

        # Get savings object from slug
        savings_object = SavingsAccount.objects.select_related('user').get(slug=savings_slug)

        # Add the budget object to the context
        context['savings'] = savings_object

        # Savings name
        context['savings_name'] = savings_object.name

        # Savings balance
        context['savings_balance'] = savings_object.balance

        try:
            # Get savings goal amount
            savings_goal_object = SavingsGoal.objects.get(savings=savings_object)
            context['savings_goal'] = savings_goal_object
            context['savings_goal_amount'] = savings_goal_object.amount
        except SavingsGoal.DoesNotExist:
            # If savings goal does not exist, add an error message to the context
            context['error_message'] = 'Savings goal data not found.'

        # Calculate the total deposits made to the SavingsAccount
        total_deposits = savings_object.deposit_set.aggregate(total_deposits=Sum('amount'))['total_deposits'] or 0

        # Calculate the total withdrawals made from the SavingsAccount
        total_withdrawals = savings_object.withdrawal_set.aggregate(total_withdrawals=Sum('amount'))[
                                'total_withdrawals'] or 0

        # Calculate number of savings account for a user
        num_savings_account = SavingsAccount.objects.aggregate(num_savings_account=Count('id'))[
                                  'num_savings_account'] or 0

        # Calculate the number of savings goals for the user
        num_savings_goal = SavingsGoal.objects.aggregate(num_savings_goal=Count('id'))['num_savings_goal'] or 0

        # Calculate the number of deposits made to the SavingsAccount
        num_deposits = savings_object.deposit_set.aggregate(num_deposits=Count('id'))['num_deposits'] or 0

        # Calculate the number of withdrawals made from the SavingsAccount
        num_withdrawals = savings_object.withdrawal_set.aggregate(num_withdrawals=Count('id'))['num_withdrawals'] or 0

        # Calculate the current balance of the SavingsAccount
        current_balance = (savings_object.balance + total_deposits) - total_withdrawals

        # Calculate the percentage left to reach savings goal
        percentage_left = round(current_balance / savings_goal_object.amount, 2) * 100

        # Define the prefetch queryset
        savings_prefetch = Prefetch('savings', queryset=SavingsAccount.objects.only('id', 'name'))

        # Get deposit_withdrawal_history
        deposits = Deposit.objects.filter(savings=savings_object).prefetch_related('savings').annotate(
            timestamp=Trunc('created_at', 'month')
        ).values('created_at').annotate(
            total_amount=Sum('amount')
        ).order_by('created_at') or 0
        print(deposits)
        withdrawals = Withdrawal.objects.filter(savings=savings_object).prefetch_related('savings').annotate(
            timestamp=Trunc('created_at', 'month')
        ).values('created_at').annotate(
            total_amount=Sum('amount')
        ).order_by('created_at') or 0
        print(withdrawals)
        labels_deposit = []
        labels_withdrawal= []
        num_labels = ['Savings Accounts', 'Deposits', 'Withdrawals', 'Savings Goals']
        num_data = [num_savings_account, num_deposits, num_withdrawals, num_savings_goal]
        deposit_data = []
        withdrawal_data = []
        for deposit in deposits:
            labels_deposit.append(deposit['created_at'].strftime('%d %B'))
            deposit_data.append(float(deposit['total_amount']))
        for withdrawal in withdrawals:
            labels_withdrawal.append(withdrawal['created_at'].strftime('%d %B'))
            withdrawal_data.append(float(withdrawal['total_amount']))

        context['labels_deposit'] = json.dumps(labels_deposit)
        context['labels_withdrawal'] = json.dumps(labels_withdrawal)
        context['num_labels'] = json.dumps(num_labels)
        context['num_data'] = json.dumps(num_data)
        context['deposit_data'] = json.dumps(deposit_data)
        context['withdrawal_data'] = json.dumps(withdrawal_data)
        context['percentage_left'] = percentage_left
        context['today'] = datetime.datetime.today()
        context['total_deposits'] = total_deposits
        context['total_withdrawals'] = total_withdrawals
        context['total_savings_transactions'] = num_deposits + num_withdrawals
        context['num_deposits'] = num_deposits
        context['num_withdrawals'] = num_withdrawals
        context['current_balance'] = current_balance

        return context


@method_decorator(login_required, name='dispatch')
class DepositListView(ListView):
    model = Deposit
    template_name = 'savings_section/savings_section_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'Deposit'}

    def get_queryset(self):
        user = self.request.user
        return Deposit.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class DepositCreateView(CreateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Add Deposit'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Deposit created successfully!')
        return reverse_lazy('savings_section:deposits_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class DepositUpdateView(UpdateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Update Deposit'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Deposit Updated successfully!')
        return reverse_lazy('savings_section:deposits_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class DepositDetailView(DetailView):
    model = Deposit
    template_name = 'savings_section/savings_section_delete.html'
    extra_context = {'detail_what': 'Deposit'}

    def get_queryset(self):
        user = self.request.user
        return Deposit.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class DepositDeleteView(DeleteView):
    model = Deposit
    template_name = 'savings_section/savings_section_delete.html'
    extra_context = {'delete_what': 'Deposit'}

    def get_queryset(self):
        user = self.request.user
        return Deposit.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Deposit deleted successfully!')
        return reverse_lazy('savings_section:deposits:list')


@method_decorator(login_required, name='dispatch')
class WithdrawalListView(ListView):
    model = Withdrawal
    template_name = 'savings_section/savings_section_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'Withdrawal'}

    def get_queryset(self):
        user = self.request.user
        return Withdrawal.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class WithdrawalCreateView(CreateView):
    model = Withdrawal
    form_class = WithdrawalForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Add Withdrawal'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Withdrawal created successfully!')
        return reverse_lazy('savings_section:withdrawals_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class WithdrawalUpdateView(UpdateView):
    model = Withdrawal
    form_class = WithdrawalForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Update Withdrawal'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Withdrawal updated successfully!')
        return reverse_lazy('savings_section:withdrawal_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class WithdrawalDetailView(DetailView):
    model = Withdrawal
    template_name = 'savings_section/savings_section_detail.html'
    extra_context = {'detail_what': 'Withdrawal'}

    def get_queryset(self):
        user = self.request.user
        return Withdrawal.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class WithdrawalDeleteView(DeleteView):
    model = Withdrawal
    template_name = 'savings_section/savings_section_delete.html'
    extra_context = {'delete_what': 'Withdrawal'}

    def get_queryset(self):
        user = self.request.user
        return Withdrawal.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Withdrawal deleted successfully!')
        return reverse_lazy('savings_section:withdrawal:list')


@method_decorator(login_required, name='dispatch')
class SavingsGoalListView(ListView):
    model = SavingsGoal
    template_name = 'savings_section/savings_section_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'SavingsGoal'}

    def get_queryset(self):
        user = self.request.user
        return SavingsGoal.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsGoalCreateView(CreateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Add SavingsGoal'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'SavingsGoal created successfully!')
        return reverse_lazy('savings_section:savings_goals_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsGoalUpdateView(UpdateView):
    model = SavingsGoal
    form_class = SavingsGoalForm
    template_name = 'savings_section/savings_section_form.html'
    extra_context = {'header': 'Update SavingsGoal'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'SavingsGoal updated successfully!')
        return reverse_lazy('savings_section:savings_goals_list')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsGoalDetailView(DetailView):
    model = SavingsGoal
    template_name = 'savings_section/savings_section_detail.html'
    extra_context = {'detail_what': 'SavingsGoal'}

    def get_queryset(self):
        user = self.request.user
        return SavingsGoal.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_protect, name='dispatch')
class SavingsGoalDeleteView(DeleteView):
    model = SavingsGoal
    template_name = 'savings_section/savings_section_delete.html'
    extra_context = {'delete_what': 'SavingsGoal'}

    def get_queryset(self):
        user = self.request.user
        return SavingsGoal.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'SavingsGoal deleted successfully!')
        return reverse_lazy('savings_section:savings_goals_list')
