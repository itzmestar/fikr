from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Balance, Transaction
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Create your tests here.


class TransactionViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test', password='test123')
        user.save()

    def test_create_tx_403(self):
        """
        Ensure can't create transaction object without authentication.
        """
        url = reverse('ledger_book:tx')
        data = {'tx_type': '+', 'amount': 500}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_tx_201(self):
        """
        Ensure we can create transaction object with authentication.
        """
        url = reverse('ledger_book:tx')
        data = {'tx_type': '+', 'amount': 500}
        user = User.objects.get(username='test')
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().tx_type, '+')


class BalanceViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='test', password='test123')
        user.save()
        Transaction.objects.create(tx_type='+', amount=500)

    def test_list_balance(self):
        """
        Ensure we can list balance object.
        """
        url = reverse('ledger_book:balance')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Balance.objects.count(), 1)
        self.assertEqual(Balance.objects.get().amount, 500)
