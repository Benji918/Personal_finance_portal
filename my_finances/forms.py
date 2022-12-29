from django import forms
from my_finances.models import Income

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
        ]
        widgets = {
            'date': DateInput()
        }