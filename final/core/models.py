from django.utils import timezone
from django.db import models

from users.models import User
from utils.constants import SILVER, TYPES, OPERATIONS, NONE


class Account(models.Model):
    number = models.IntegerField(unique=True)
    balance = models.FloatField(null=True)
    min_amount = models.FloatField(null=True)
    opened_date = models.DateTimeField(default=timezone.now)
    account_type = models.PositiveSmallIntegerField(choices=TYPES, default=SILVER)
    monthly_fee = models.FloatField(null=True)
    description = models.TextField(max_length=300, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account')

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f'{self.number}: {self.owner}'


class Transaction(models.Model):
    amount = models.IntegerField()
    operation_type = models.CharField(max_length=10, choices=OPERATIONS, default=NONE)
    created_at = models.DateTimeField(default=timezone.now)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction')

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'{self.amount}, {self.account}'

