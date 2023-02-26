from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Category, Transaction, Budget
from .forms import CategoryForm, TransactionForm, BudgetForm

@method_decorator(login_required, name='dispatch')
class ListView(View):
    template_name = 'budget/home.html'

    def get(self, request):
        categories = Category.objects.filter(user=request.user)
        transactions = Transaction.objects.filter(user=request.user).order_by('-date')
        budgets = Budget.objects.filter(user=request.user).order_by('-start_date')

        context = {
            'categories': categories,
            'transactions': transactions,
            'budgets': budgets,
        }
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class BudgetCreateView(View):
    form_class = BudgetForm
    template_name = 'budget/form.html'
    title = 'Add Budget'

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'Budget has been created.')
            return redirect('home')
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class BudgetUpdateView(View):
    form_class = BudgetForm
    template_name = 'budget/form.html'
    title = 'Edit Budget'

    def get(self, request, pk):
        budget = get_object_or_404(Category, pk=pk, user=request.user)
        form = self.form_class(instance=budget)
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        budget = get_object_or_404(Budget, pk=pk, user=request.user)
        form = self.form_class(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            messages.success(request, 'Budget has been updated.')
            return redirect('home')
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

@login_required
def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    budget.delete()
    messages.success(request, 'budget has been deleted.')
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(View):
    form_class = CategoryForm
    template_name = 'budget/form.html'
    title = 'Add Category'

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category has been created.')
            return redirect('home')
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(View):
    form_class = CategoryForm
    template_name = 'budget/form.html'
    title = 'Edit Category'

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk, user=request.user)
        form = self.form_class(instance=category)
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk, user=request.user)
        form = self.form_class(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been updated.')
            return redirect('home')
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    category.delete()
    messages.success(request, 'Category has been deleted.')
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class TransactionCreateView(View):
    form_class = TransactionForm
    template_name = 'budget/form.html'
    title = 'Add Transaction'

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transaction created Successfully!')
            return redirect('home')
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class TransactionUpdateView(View):
    form_class = TransactionForm
    template_name = 'budget/form.html'
    title = 'Edit Category'

    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        form = self.form_class(instance=transaction)
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        form = self.form_class(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction has been updated.')
            return redirect('home')
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    transaction.delete()
    messages.success(request, 'Transaction has been deleted.')
    return redirect('home')
