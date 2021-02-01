from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Source, Person, Balance, Transaction
from .serializers import SourceSerializer, PersonSerializer
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


def index(request):
    tx_list = Transaction.objects.all()
    context = {
        'tx_list': tx_list,
    }
    return render(request, 'ledger_book/index.html', context)


# API views:


class SourceView(ListAPIView):
    """
    View to get Source & Source creation history
    """

    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class PersonView(ListAPIView):
    """
    View to get Person & Person creation history
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


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

