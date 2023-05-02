from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import Profile, CustomUser, SMSCode
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox



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
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

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
        instance.username = self.cleaned_data['email']
        if commit:
            instance.save()
        return instance


# for profile update
class UpdateProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    avatar = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), max_length=1000, required=False)

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs['class'] = 'form-control form-control-user'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Email already exists.')
        return email

    def save(self, commit=True):
        user = super(UpdateProfileForm, self).save(commit=False)
        user.save()
        profile = user.profile
        if self.cleaned_data.get('avatar'):
            profile.avatar = self.cleaned_data['avatar']
        if self.cleaned_data.get('bio'):
            profile.bio = self.cleaned_data['bio']
        profile.save()
        return user


# Password change
class Set_Password_Form(SetPasswordForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = CustomUser
        fields = ['new_password1', 'new_password2']


class Password_Reset_Form(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)




class SMSCodeForm(forms.ModelForm):
    class Meta:
        model = SMSCode
        fields = ['number']

    number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Enter verification code'
    }), label='SMS code')

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)  # pop the user ID from the keyword arguments
        super().__init__(*args, **kwargs)
        self.user_id = user_id  # save the user ID as an instance variable

    def sms_validate(self):
        user_id = self.user_id
        if user_id is None:
            raise forms.ValidationError(_('Invalid user ID.'))
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError(_('Invalid user ID.'))
        num = self.cleaned_data.get('number')
        if num != str(user.smscode.number):
            raise forms.ValidationError(_('Invalid SMS verification code. Try again!'))
        return num
