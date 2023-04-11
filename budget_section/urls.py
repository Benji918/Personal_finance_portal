from django.urls import path

from budget_section.views import CategoryCreateView, TransactionUpdateView, TransactionCreateView, CategoryUpdateView, \
    BudgetCreateView, BudgetUpdateView, BudgetListView, CategoryListView, BudgetDeleteView, \
    CategoryDeleteView, TransactionListView, TransactionDeleteView, CategoryDetailView, TransactionDetailView, \
    BudgetDetailView, GetSummaryTiles

app_name = 'budget_section'

urlpatterns = [
    # CATEGORIES URLS
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/detail/<slug:slug>/', CategoryDetailView.as_view(), name='category_details'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category_delete'),
    # TRANSACTIONS URLS
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction/update/<slug:slug>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/detail/<slug:slug>/', TransactionDetailView.as_view(), name='transaction_details'),
    path('transaction/delete/<slug:slug>/', TransactionDeleteView.as_view(), name='transaction_delete'),
    # BUDGET URLS
    path('budgets/', BudgetListView.as_view(), name='budget_list'),
    path('budget/create/', BudgetCreateView.as_view(), name='budget_create'),
    path('budget/update/<slug:slug>/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budget/detail/<slug:slug>/', BudgetDetailView.as_view(), name='budget_details'),
    path('budget/delete/<slug:slug>/', BudgetDeleteView.as_view(), name='budget_delete'),
    # DASHBOARD URLS
    path('budget/current_period/budget_name/<slug:slug>', GetSummaryTiles.as_view(), name='budget_summary'),
    # path('budget/current_period/<slug:slug>',  BudgetCategoryView.as_view(), name='budget-category'),

]
