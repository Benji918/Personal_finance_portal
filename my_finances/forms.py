from django import forms
from my_finances.models import Income, Outcome, Balance
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = [
            'value',
            'date',
            'type',
            'repetitive',
            'repetition_interval',
            'repetition_time',
            'repetition_end',
            'comment'
        ]

    date = forms.DateField(widget=DateInput, initial=date.today())
    repetition_end = forms.DateField(widget=DateInput, required=False)

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['value', 'date', 'type', 'repetitive', 'repetition_interval', 'repetition_time', 'repetition_end',
                  'comment']

    date = forms.DateField(widget=DateInput, initial=date.today())
    repetition_end = forms.DateField(widget=DateInput, required=False)

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['value', 'date', 'type', 'comment']

    date = forms.DateField(widget=DateInput, initial=date.today())
