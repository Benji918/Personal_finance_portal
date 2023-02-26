from django.contrib import admin
from .models import Category, Transaction, BudgetTransaction, Budget

# Register your models here.
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(BudgetTransaction)
admin.site.register(Budget)

