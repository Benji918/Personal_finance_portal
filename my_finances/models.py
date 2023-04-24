from django.db import models
from django.conf import settings


# Create your models here.
class Income(models.Model):
    class ITypes(models.IntegerChoices):
        SAL = 1, "SALARY"
        BON = 2, "BONUS"
        GIF = 3, "GIFT"
        OTH = 4, "OTHER"
        SAV = 5, "SAVINGS"

    class RInterval(models.IntegerChoices):
        NA = 1, 'N/A'
        DAY = 2, 'DAYS'
        WEK = 3, 'WEEKS'
        MON = 4, 'MONTHS'
        YEA = 5, 'YEARS'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_incomes')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=ITypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default=0)
    repetition_end = models.DateField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'incomes'


class Outcome(models.Model):
    class OTypes(models.IntegerChoices):
        REN = 1, "RENT"
        BIL = 2, "BILLS"
        CAR = 3, "CAR"
        TRA = 4, "TRAVEL"
        HEA = 5, "HEALTH"
        GRO = 6, "GROCERIES"
        FUN = 7, "FUN"
        CLO = 8, "CLOTHES"
        CHA = 9, "CHARITY"
        SAV = 10, "SAVINGS"

    class RInterval(models.IntegerChoices):
        NA = 1, 'N/A'
        DAY = 2, 'DAYS'
        WEK = 3, 'WEEKS'
        MON = 4, 'MONTHS'
        YEA = 5, 'YEARS'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_outcomes')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=OTypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default=0)
    repetition_end = models.DateField(null=True)
    comment = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Outcome {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = 'outcomes'


class Balance(models.Model):
    class BType(models.IntegerChoices):
        CUR = 1, "CURRENT"
        SAV = 2, "SAVINGS"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_balances')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.PositiveSmallIntegerField(choices=BType.choices)
    date = models.DateField()
    comment = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Balance {self.id} - {self.type}'

    class Meta:
        verbose_name_plural = 'balances'
