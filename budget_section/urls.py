from django.urls import path
from budget_section import views
from budget_section.views import CategoryCreateView, TransactionUpdateView, TransactionCreateView, CategoryUpdateView, \
    BudgetCreateView, BudgetUpdateView

app_name = 'budget_section'

urlpatterns = [
    # path('categories/', CategoryList.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.delete_category, name='category_delete'),
    # path('transactions/', TransactionList.as_view(), name='transaction_list'),
    path('transaction/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/<int:pk>/delete/', views.delete_transaction, name='transaction_delete'),
    # path('budgets', BudgetListView.as_view(), name='budget_list'),
    path('budget/create/', BudgetCreateView.as_view(), name='budget_create'),
    path('budget/<int:pk>/update/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budget/<int:pk>/delete/', views.delete_budget, name='budget_delete')

]
