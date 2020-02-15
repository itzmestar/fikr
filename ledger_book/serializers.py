from rest_framework import serializers
from .models import Transaction, Balance


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['tx_id', 'created', 'tx_type', 'from_or_to', 'amount', 'description']


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['created', 'amount']
