from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _

from .models import Profile, CustomUser


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
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={
        # 'class': 'form-control form-control-user',
        'placeholder': 'Phone number',
    }))
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Password'
    }), label='Password')
    password2 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Confirm Password'
    }), label='Confirm password')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()

        # Ensure that the email is unique
        email = cleaned_data.get('email')
        if email and CustomUser.objects.filter(email=email).exists():
            self.add_error('email', 'A user with this email already exists.')

        # Ensure that the first name is unique
        first_name = cleaned_data.get('first_name')
        if first_name and CustomUser.objects.filter(first_name=first_name).exists():
            self.add_error('first_name', 'A user with this first name already exists.')

        # Ensure that the last name is unique
        last_name = cleaned_data.get('last_name')
        if last_name and CustomUser.objects.filter(last_name=last_name).exists():
            self.add_error('last_name', 'A user with this last name already exists.')

        return cleaned_data

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number:
            raise forms.ValidationError(_('This field is required.'))
        if not phone_number.is_valid():
            raise forms.ValidationError(_('Invalid phone number. Try again!'))
        return phone_number

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance


# for profile update
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


# Password change
class Set_Password_Form(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ['new_password1', 'new_password2']


class Password_Reset_Form(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
