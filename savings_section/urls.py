from django.urls import path

from .views import SavingsAccountListView, SavingsAccountCreateView, \
    SavingsAccountUpdateView, SavingsAccountDeleteView, SavingsAccountDetailView, SavingsAccountSummaryTiles, \
    DepositListView, DepositUpdateView, DepositDeleteView, DepositCreateView, DepositDetailView, \
    WithdrawalListView, WithdrawalDetailView, WithdrawalCreateView, WithdrawalUpdateView, WithdrawalDeleteView, \
    SavingsGoalDetailView, SavingsGoalListView, SavingsGoalCreateView, SavingsGoalDeleteView, SavingsGoalUpdateView

app_name = 'savings_section'

urlpatterns = [
    # SAVINGS_ACCOUNT URLS
    path('savings_accounts/', SavingsAccountListView.as_view(), name='savings_list'),
    path('savings_create/', SavingsAccountCreateView.as_view(), name='savings_create'),
    path('savings_update/<slug:slug>/', SavingsAccountUpdateView.as_view(), name='savings_update'),
    path('savings_detail/<slug:slug>/', SavingsAccountDetailView.as_view(), name='savings_detail'),
    path('savings_delete/<slug:slug>/', SavingsAccountDeleteView.as_view(), name='savings_delete'),

    # DEPOSIT URLS
    path('deposits/', DepositListView.as_view(), name='deposits_list'),
    path('deposit_create/', DepositCreateView.as_view(), name='deposit_create'),
    path('deposit_update/<slug:slug>/', DepositUpdateView.as_view(), name='deposit_update'),
    path('deposit_detail/<slug:slug>/', DepositDetailView.as_view(), name='deposit_detail'),
    path('deposit_delete/<slug:slug>/', DepositDeleteView.as_view(), name='deposit_delete'),

    # WITHDRAWAL URLS
    path('withdrawals/', WithdrawalListView.as_view(), name='withdrawals_list'),
    path('withdrawal_create/', WithdrawalCreateView.as_view(), name='withdrawal_create'),
    path('withdrawal_update/<slug:slug>/', WithdrawalUpdateView.as_view(), name='withdrawal_update'),
    path('withdrawal_detail/<slug:slug>/', WithdrawalDetailView.as_view(), name='withdrawal_detail'),
    path('withdrawal_delete/<slug:slug>/', WithdrawalDeleteView.as_view(), name='withdrawal_delete'),

    # SAVINGS_GOAL URLS
    path('savings_goals/', SavingsGoalListView.as_view(), name='savings_goals_list'),
    path('savings_goal_create/', SavingsGoalCreateView.as_view(), name='savings_goal_create'),
    path('savings_goal_update/<slug:slug>/', SavingsGoalUpdateView.as_view(), name='savings_goal_update'),
    path('savings_goal_detail/<slug:slug>/', SavingsGoalDetailView.as_view(), name='savings_goal_detail'),
    path('savings_goal_delete/<slug:slug>/', SavingsGoalDeleteView.as_view(), name='savings_goal_delete'),

    # DASHBOARD URLS
    path('savings_accounts/current_period/<slug:slug>', SavingsAccountSummaryTiles.as_view(), name='savings_summary'),

]