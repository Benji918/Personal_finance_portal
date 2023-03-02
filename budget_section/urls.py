from django.urls import path
from budget_section import views
from budget_section.views import CategoryCreateView, TransactionUpdateView, TransactionCreateView, CategoryUpdateView, \
    BudgetCreateView, BudgetUpdateView, BudgetListView, CategoryListView, BudgetDeleteView, \
    CategoryDeleteView, TransactionListView

app_name = 'budget_section'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction/update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),

    path('budgets', BudgetListView.as_view(), name='budget_list'),
    path('budget/create/', BudgetCreateView.as_view(), name='budget_create'),
    path('budget/update/<int:pk>/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budget/delete/<int:pk>/',  BudgetDeleteView.as_view(), name='budget_delete')

]
