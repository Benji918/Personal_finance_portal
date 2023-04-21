from django.contrib import messages
from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
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
        savings_object = SavingsAccount.objects.get(slug=savings_slug)

        # Add the budget object to the context
        context['savings'] = savings_object

        # Savings name
        context['savings_name'] = savings_object.name

        # Savings balance
        context['savings_balance'] = savings_object.balance

        # Calculate the total deposits made to the SavingsAccount
        total_deposits = savings_object.deposit_set.aggregate(total_deposits=Sum('amount'))['total_deposits'] or 0

        # Calculate the total withdrawals made from the SavingsAccount
        total_withdrawals = savings_object.withdrawal_set.aggregate(total_withdrawals=Sum('amount'))[
                                'total_withdrawals'] or 0

        # Calculate the number of deposits made to the SavingsAccount
        num_deposits = savings_object.deposit_set.aggregate(num_deposits=Count('id'))['num_deposits'] or 0

        # Calculate the number of withdrawals made from the SavingsAccount
        num_withdrawals = savings_object.withdrawal_set.aggregate(num_withdrawals=Count('id'))['num_withdrawals'] or 0

        # Calculate the current balance of the SavingsAccount
        current_balance = savings_object.balance + total_deposits - total_withdrawals

        context['total_deposits'] = total_deposits
        context['total_withdrawals'] = total_withdrawals
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
