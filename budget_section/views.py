from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
        # categories = Category.objects.filter(user=request.user)
        # transactions = Transaction.objects.filter(user=request.user).order_by('-date')
        return Budget.objects.filter(user=user).order_by('-start_date')


@method_decorator(login_required, name='dispatch')
class BudgetCreateView(View):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget_section/category_transaction_budget_form.html'
    extra_context = {'header': 'Add budget'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Budget created successfully!')
        return reverse_lazy('budget_section:budget_list')


@method_decorator(login_required, name='dispatch')
class BudgetUpdateView(View):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget_section/category_transaction_budget_list.html'
    extra_context = {'header': 'Update Budget'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Budget updated successfully!')
        return reverse_lazy('budget_section:budget_update')


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
class CategoryCreateView(View):
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
class CategoryUpdateView(View):
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
        messages.success(self.request, 'Category created successfully!')
        return reverse_lazy('budget_section:category_list')


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
    context_object_name = 'transactions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get total amount spent in the last 7 days
        today = datetime.date.today()
        week_ago = today - timedelta(days=7)
        context['total_spent_last_week'] = Transaction.objects.filter(date__range=[week_ago, today]).aggregate(
            Sum('amount'))['amount__sum'] or 0

        # Get average amount spent per category
        context['average_spent_per_category'] = Transaction.objects.values('category__name').annotate(
            average_spent=Avg('amount')).order_by('-date')[:5]

        # Get total amount spent per category
        context['total_spent_per_category'] = Transaction.objects.values('category__name').annotate(
            total_spent=Sum('amount')).order_by('-date')[:5]

        # Get the total categories
        context['total_categories'] = Category.objects.count()

        return context


@method_decorator(login_required, name='dispatch')
class TransactionCreateView(View):
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
class TransactionUpdateView(View):
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
