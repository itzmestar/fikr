from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Balance, Transaction
from .serializers import BalanceSerializer, TransactionSerializer

from django.http import HttpResponse, JsonResponse

'''
def balance_view(request):
    if request.method == 'GET':
        snippets = Balance.objects.all()
        serializer = BalanceSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
'''

# Create your views here.


class BalanceView(ListAPIView):
    """
    View to get balance & balance history
    """

    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class TransactionView(ListCreateAPIView):
    """
    View to create and view Transaction history
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

