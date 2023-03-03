from django import forms
from .models import Category, Transaction, Budget
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'budget', 'date', 'notes']

    date = forms.DateField(widget=DateInput, initial=date.today())

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'amount', 'start_date', 'end_date']

    start_date = forms.DateField(widget=DateInput, initial=date.today())
    end_date = forms.DateField(widget=DateInput)



