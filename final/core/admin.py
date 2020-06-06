import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
from django.db.models.functions import TruncDay

from core.models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'balance',
        'account_type',
        'owner'
    )

    fields = ('number', 'balance', 'account_type', 'min_amount', 'opened_date', 'monthly_fee', 'description', 'owner')
    readonly_fields = ('owner',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'amount',
        'operation_type',
        'created_at',
        'account'
    )

    fields = ('amount', 'operation_type', 'created_at', 'account')
    readonly_fields = ('account',)
