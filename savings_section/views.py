from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
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
        return SavingsAccount.objects.filter(account_holder=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
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
class SavingsAccountDetailView(DetailView):
    model = SavingsAccount
    template_name = 'savings_section/savings_section_detail.html'
    extra_context = {'detail_what': 'Savings'}

    def get_queryset(self):
        user = self.request.user
        return SavingsAccount.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
class SavingsAccountDeleteView(DeleteView):
    model = SavingsAccount
    template_name = 'savings_section/savings_section_delete.html'
    extra_context = {'delete_what': 'Savings'}

    def get_queryset(self):
        user = self.request.user
        return SavingsAccount.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Savings user deleted successfully!')
        return reverse_lazy('savings_section:savings:list')

@method_decorator(login_required, name='dispatch')
class SavingsAccountSummaryTiles(ListView):
    pass


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
class DepositDetailView(DetailView):
    model = Deposit
    template_name = 'savings_section/savings_section_delete.html'
    extra_context = {'detail_what': 'Deposit'}

    def get_queryset(self):
        user = self.request.user
        return Deposit.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
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
class DepositSummaryTiles(ListView):
    pass


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
class WithdrawalDetailView(DetailView):
    model = Withdrawal
    template_name = 'savings_section/savings_section_detail.html'
    extra_context = {'detail_what': 'Withdrawal'}

    def get_queryset(self):
        user = self.request.user
        return Withdrawal.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
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
class WithdrawalSummaryTiles(ListView):
    pass


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
class SavingsGoalDetailView(DetailView):
    model = SavingsGoal
    template_name = 'savings_section/savings_section_detail.html'
    extra_context = {'detail_what': 'SavingsGoal'}

    def get_queryset(self):
        user = self.request.user
        return SavingsGoal.objects.filter(user=user).order_by('-id')


@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class SavingsGoalSummaryTiles(ListView):
    pass
