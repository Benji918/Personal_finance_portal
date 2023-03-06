from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Avg
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Category, Transaction, Budget
from .forms import CategoryForm, TransactionForm, BudgetForm

# BUDGET
@method_decorator(login_required, name='dispatch')
class BudgetListView(ListView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'Budget'}

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(user=user).order_by('-start_date')


@method_decorator(login_required, name='dispatch')
class BudgetCreateView(CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add Budget'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Budget created successfully!')
        return reverse_lazy('budget_section:budget_list')


@method_decorator(login_required, name='dispatch')
class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Update Budget'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Budget updated successfully!')
        return reverse_lazy('budget_section:budget_list')

@method_decorator(login_required, name='dispatch')
class BudgetDetailView(DetailView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_detail.html'
    extra_context = {'detail_what': 'Budget'}

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(user=user).order_by('-id')

@method_decorator(login_required, name='dispatch')
class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_delete.html'
    extra_context = {'delete_what': 'Budget'}

    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Budget deleted successfully!')
        return reverse_lazy('budget_section:budget_list')

# CATEGORY
@method_decorator(login_required, name='dispatch')
class CategoryListView(ListView):
    model = Category
    template_name = 'budget_section/category_transaction_budget_list.html'
    paginate_by = 100
    extra_context = {'list_what': 'Category'}

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user).order_by('-id')

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add Category'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Category created successfully!')
        return reverse_lazy('budget_section:category_list')


@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Update Category'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Category updated successfully!')
        return reverse_lazy('budget_section:category_list')

@method_decorator(login_required, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'budget_section/category_transaction_budget_detail.html'
    extra_context = {'detail_what': 'Category'}

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Budget
    template_name = 'budget_section/category_transaction_budget_delete.html'
    extra_context = {'delete_what': 'Category'}

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Category deleted successfully!')
        return reverse_lazy('budget_section:category_list')


@method_decorator(login_required, name='dispatch')
class TransactionListView(ListView):
    model = Transaction
    template_name = 'budget_section/category_transaction_budget_list.html'
    extra_context = {'list_what': 'Transaction'}

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user).order_by('-date')


@method_decorator(login_required, name='dispatch')
class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add Transaction'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Transaction created successfully!')
        return reverse_lazy('budget_section:transaction_list')


@method_decorator(login_required, name='dispatch')
class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Update Transaction'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Transaction updated successfully!')
        return reverse_lazy('budget_section:transaction_list')


@method_decorator(login_required, name='dispatch')
class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'budget_section/category_transaction_budget_detail.html'
    extra_context = {'detail_what': 'Transaction'}

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user).order_by('-date')


@method_decorator(login_required, name='dispatch')
class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'budget_section/category_transaction_budget_delete.html'
    extra_context = {'delete_what': 'Transaction'}

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Transaction deleted successfully!')
        return reverse_lazy('budget_section:transaction_list')


def get_summary_tiles(request, pk=id):
    # today = datetime.today()
    # Get the budget ID from the URL parameters
    budget = Budget.objects.get(id=pk, user=request.user)
    print(budget.amount)
    # Get the total number of transactions in the budget
    total_budget_transactions = Transaction.objects.filter(budget=budget).count()
    # Get the total amount spent in the budget
    total_amount_spent = Transaction.objects.filter(budget=budget).aggregate(Sum('amount'))['amount__sum'] or 0
    # Get the total budget amount
    total_budget = budget.amount
    print(total_budget)
    # Calculate the percentage spent
    if total_budget > 0:
        percentage_spent = round(total_amount_spent / budget.amount * 100, 2)
    else:
        percentage_spent = 0
    return JsonResponse({
        'budget_balance': budget.amount,
        'budget_date': budget.created_at,
        'total_budget_transactions': total_budget_transactions,
        'budget_amount_left': budget.amount - total_amount_spent,
        'budget_amount_left_in_percentage': percentage_spent,


    })

class GetSummaryTiles(ListView):
    model = Budget
    template_name = 'budget_section/current_period.html'
    context_object_name = 'budget_data'

    def get_queryset(self):
        # Get the budget from the URL parameters
        budget_id = self.kwargs['pk']

        # Get the budget object
        budget = Budget.objects.get(id=budget_id)

        # Filter transactions by the budget
        transactions = Transaction.objects.filter(budget=budget)

        return transactions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the budget ID from the URL parameters
        budget_id = self.kwargs['pk']

        # Get the budget object
        budget = Budget.objects.get(id=budget_id)

        # Add the budget object to the context
        context['budget'] = budget

        # Get the total amount spent in the budget
        context['total_spent'] = Transaction.objects.filter(budget=budget).aggregate(Sum('amount'))['amount__sum'] or 0

        # Get the total number of transactions in the budget
        context['total_budget_transactions'] = Transaction.objects.filter(budget=budget).count()

        # Get the total budget amount
        context['total_budget'] = budget.amount

        # Budget amount spent
        context['budget_amount_spent'] = context['total_budget'] - context['total_spent']

        # Calculate the percentage spent
        if context['total_budget'] > 0:
            percentage_spent = round(context['total_spent'] / context['total_budget'] * 100, 2)
        else:
            percentage_spent = 0

        # Add the percentage spent to the context
        context['percentage_spent'] = percentage_spent

        return context

