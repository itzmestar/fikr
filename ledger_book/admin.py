from django.contrib import admin

# Register your models here.
from .models import Person, Source, Transaction, Balance


class SourceAdmin(admin.ModelAdmin):
    list_display = ('created', 'name')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('created', 'name')


class TransactionAdmin(admin.ModelAdmin):
    fields = ['created', 'tx_type', 'person', 'source', 'amount', 'description']
    list_display = ('created', 'tx_type', 'person', 'source', 'amount', 'description')
    list_filter = ['created', 'tx_type', 'person', 'source']


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('created', 'amount')


admin.site.register(Source, SourceAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Balance, BalanceAdmin)
