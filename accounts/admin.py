from django.contrib import admin
from .models import Profile, CustomUser, SMSCode
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# Register your models here.
admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(SMSCode)
