from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Balance
from .serializers import BalanceSerializer

from django.http import HttpResponse, JsonResponse

'''
def balance_view(request):
    if request.method == 'GET':
        snippets = Balance.objects.all()
        serializer = BalanceSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
'''

# Create your views here.
class BalanaceView(ListAPIView):
    """
    View to get balance & balance history
    """

    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
