from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class SavingsAccount(models.Model):
    account_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'SavingsAccount name - {self.name}'


class Deposit(models.Model):
    account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Deposit name - {self.name}'


class Withdrawal(models.Model):
    account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Withdrawal name - {self.name}'


class SavingsGoal(models.Model):
    account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'SavingsGoal name - {self.name}'