from django.urls import path
from my_finances import views

app_name = 'my_finances'

urlpatterns = [
    # Income_urls
    path('income_list/', views.IncomeListVIew.as_view(), name='income_list'),
    path('income_detail/<pk>', views.IncomeDetailView.as_view(), name='income_detail'),
    path('income_create/', views.IncomeCreateView.as_view(), name='income_create'),
    path('income_update/<pk>', views.IncomeUpdateView.as_view(), name='income_update'),
    path('income_delete/<pk>', views.IncomeDeleteView.as_view(), name='income_delete'),
    # Outcome_urls
    path('outcome_list/', views.OutcomeListVIew.as_view(), name='outcome_list'),
    path('outcome_detail/<pk>', views.OutcomeDetailView.as_view(), name='outcome_detail'),
    path('outcome_create/', views.OutcomeCreateView.as_view(), name='outcome_create'),
    path('outcome_update/<pk>', views.OutcomeUpdateView.as_view(), name='outcome_update'),
    path('outcome_delete/<pk>', views.OutcomeDeleteView.as_view(), name='outcome_delete'),
]
