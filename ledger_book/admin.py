from django.contrib import admin

# Register your models here.
from .models import Source, Transaction, Balance


class SourceAdmin(admin.ModelAdmin):
    pass


class TransactionAdmin(admin.ModelAdmin):
    fields = ['created', 'tx_type', 'from_or_to', 'amount', 'description']


class BalanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Source, SourceAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Balance, BalanceAdmin)
