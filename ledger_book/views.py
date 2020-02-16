from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Balance
from .serializers import BalanceSerializer

# Create your views here.
class BalanaceView(ListAPIView):
    """
    View to get balance & balance history
    """

    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer