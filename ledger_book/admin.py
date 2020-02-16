from django.contrib import admin

# Register your models here.
from .models import Source, Transaction, Balance


class SourceAdmin(admin.ModelAdmin):
    list_display = ('created', 'name')


class TransactionAdmin(admin.ModelAdmin):
    fields = ['created', 'tx_type', 'from_or_to', 'amount', 'description']
    list_display = ('created', 'tx_type', 'from_or_to', 'amount', 'description')
    list_filter = ['created', 'tx_type', 'from_or_to']


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('created', 'amount')


admin.site.register(Source, SourceAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Balance, BalanceAdmin)
