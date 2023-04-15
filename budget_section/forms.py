from datetime import date
from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Transaction, Budget


class DateInput(forms.DateInput):
    input_type = 'date'


class CategoryForm(forms.ModelForm):
    def is_valid(self):
        is_valid = super().is_valid()
        # add custom validation logic for the name field
        if 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            if name.startswith('X'):  # name should not start with 'X'
                self.add_error('name', 'Name should not start with X')
                is_valid = False

        return is_valid

    class Meta:
        model = Category
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):  # check if name contains any digits
            raise ValidationError("Name should not contain numbers")
        return name


class TransactionForm(forms.ModelForm):
    def is_valid(self):
        is_valid = super().is_valid()
        # add custom validation logic for the name field
        if 'title' in self.cleaned_data:
            name = self.cleaned_data['title']
            if name.startswith('X'):  # name should not start with 'X'
                self.add_error(field='title', error='Name should not start with X')
                is_valid = False
        if 'amount' in self.cleaned_data:
            amount = self.cleaned_data['amount']
            budget = self.cleaned_data['budget']
            if amount <= 0:
                self.add_error(field='amount', error='Amount must be greater than zero')
                is_valid = False
            elif amount != int(amount):
                self.add_error(field='amount', error='Amount must be a whole number')
                is_valid = False
            elif amount > budget.amount:
                self.add_error(field='amount', error='Amount cannot be greater than budget amount')
                is_valid = False
        return is_valid

    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'category', 'budget', 'date', 'notes']

    date = forms.DateField(widget=DateInput, initial=date.today())

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero")
        elif amount != int(amount):
            raise ValidationError("Amount must be a whole number")
        return amount


class BudgetForm(forms.ModelForm):
    def is_valid(self):
        is_valid = super().is_valid()
        # add custom validation logic for the name field
        if 'name' in self.cleaned_data:
            name = self.cleaned_data['name']
            if name.startswith('X'):  # name should not start with 'X'
                self.add_error(field='name', error='Name should not start with X')
                is_valid = False
        if 'start_date' in self.cleaned_data and 'end_date' in self.cleaned_data:
            start_date = self.cleaned_data['start_date']
            end_date = self.cleaned_data['end_date']
            if end_date <= start_date:
                self.add_error(field='end_date', error='End date must be greater than start date')
                is_valid = False
            if start_date >= end_date:
                self.add_error(field='start_date', error='Start date must be less than end date')
                is_valid = False

        return is_valid

    class Meta:
        model = Budget
        fields = ['name', 'amount', 'start_date', 'end_date']

    start_date = forms.DateField(widget=DateInput, initial=date.today())
    end_date = forms.DateField(widget=DateInput)

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero")
        elif amount != int(amount):
            raise ValidationError("Amount must be a whole number")
        return amount

    def clean_end_date(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date <= start_date:
            raise ValidationError("End date must be greater than start date")
        if start_date >= end_date:
            raise ValidationError("Start date must be less than end date")

        return end_date
