from django.contrib import admin
from my_finances import models

# Register your models here.
admin.site.register(models.Income)
admin.site.register(models.Outcome)
admin.site.register(models.Balance)