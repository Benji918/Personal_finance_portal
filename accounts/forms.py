from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUSerCreationForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Last Name'
    }))
    email = forms.Field(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Email'
    }))
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Password'
    }), label='Password')
    password2 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Confirm Password'
    }), label='Confirm password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance



