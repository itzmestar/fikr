from rest_framework import serializers
from .models import Transaction, Balance


class TransactionSerializer(serializers.ModelSerializer):
    source = serializers.StringRelatedField()
    person = serializers.StringRelatedField()
    class Meta:
        model = Transaction
        fields = ['tx_id', 'created', 'tx_type', 'source', 'person', 'amount', 'description']
        #fields = '__all__'
        #depth = 1


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        #fields = ['created', 'amount']
        fields = '__all__'
