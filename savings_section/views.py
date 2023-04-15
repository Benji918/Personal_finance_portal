from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SavingsAccount, Deposit, Withdrawal, SavingsGoal
from .forms import SavingsGoalForm, WithdrawalForm, DepositForm, SavingsAccount

@method_decorator(login_required, name='dispatch')
class SavingsAccountListView(ListView):
    model = SavingsAccount
    template_name = 'savings_section/savings_section_list'
    paginate_by = 100
    extra_context = {'list_what': 'Savings'}

    def get_queryset(self):
        user = self.request.user
        return SavingsAccount.objects.filter(user=user).order_by('-id')


class SavingsAccountCreateView(CreateView):
    model = SavingsAccount
    form_class = Sa




class SavingsAccountUpdateView(UpdateView):
    model = SavingsAccount
    fields = ['account_holder', 'name', 'balance']
    success_url = reverse_lazy('savings_account_list')


class SavingsAccountDeleteView(DeleteView):
    model = SavingsAccount
    success_url = reverse_lazy('savings_account_list')


class DepositListView(ListView):
    model = Deposit


class DepositCreateView(CreateView):
    model = Deposit
    fields = ['account', 'name', 'amount']
    success_url = reverse_lazy('deposit_list')


class DepositUpdateView(UpdateView):
    model = Deposit
    fields = ['account', 'name', 'amount']
    success_url = reverse_lazy('deposit_list')


class DepositDeleteView(DeleteView):
    model = Deposit
    success_url = reverse_lazy('deposit_list')


class WithdrawalListView(ListView):
    model = Withdrawal


class WithdrawalCreateView(CreateView):
    model = Withdrawal
    fields = ['account', 'name', 'amount']
    success_url = reverse_lazy('withdrawal_list')


class WithdrawalUpdateView(UpdateView):
    model = Withdrawal
    fields = ['account', 'name', 'amount']
    success_url = reverse_lazy('withdrawal_list')


class WithdrawalDeleteView(DeleteView):
    model = Withdrawal
    success_url = reverse_lazy('withdrawal_list')


class SavingsGoalListView(ListView):
    model = SavingsGoal


class SavingsGoalCreateView(CreateView):
    model = SavingsGoal
    fields = ['account', 'name', 'amount']
    success_url = reverse_lazy('savings_goal_list')


class SavingsGoalUpdateView(UpdateView):
    model = SavingsGoal
    fields = ['account', 'name', 'amount']
    success_url = reverse_lazy('savings_goal_list')


class SavingsGoalDeleteView(DeleteView):
    model = SavingsGoal
    success_url = reverse_lazy('savings_goal_list')
# Create your views here.
