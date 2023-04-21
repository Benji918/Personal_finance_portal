# Register your models here.
from django.contrib import admin
from .models import SavingsAccount, Deposit, Withdrawal, SavingsGoal

admin.site.register(SavingsAccount)
admin.site.register(SavingsGoal)
admin.site.register(Deposit)
admin.site.register(Withdrawal)