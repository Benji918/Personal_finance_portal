from django.conf import settings
from django.db import models
from django.utils.text import slugify


# Create your models here.
class SavingsAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SavingsAccount name - {self.name}'


class Deposit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Deposit name - {self.name}'


class Withdrawal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Withdrawal name - {self.name}'


class SavingsGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SavingsGoal name - {self.name}'
