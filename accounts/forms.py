from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm


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
