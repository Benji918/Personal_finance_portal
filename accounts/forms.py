from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox

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

    def clean(self):
        cleaned_data = super().clean()

        # Ensure that the email is unique
        email = cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            self.add_error('email', 'A user with this email already exists.')

        # Ensure that the first name is unique
        first_name = cleaned_data.get('first_name')
        if first_name and User.objects.filter(first_name=first_name).exists():
            self.add_error('first_name', 'A user with this first name already exists.')

        # Ensure that the last name is unique
        last_name = cleaned_data.get('last_name')
        if last_name and User.objects.filter(last_name=last_name).exists():
            self.add_error('last_name', 'A user with this last name already exists.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance


# for profile update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


# Password change
class Set_Password_Form(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class Password_Reset_Form(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
