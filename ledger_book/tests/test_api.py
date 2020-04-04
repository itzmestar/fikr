from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ledger_book.models import Balance, Transaction
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
import time

# Create your tests here.


class TransactionViewTests(APITestCase):
    user = 'test'
    password = 'test123'
    url = reverse('ledger_book:tx')

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username=TransactionViewTests.user, password=TransactionViewTests.password)

    def test_create_tx_401(self):
        """
        Ensure can't create transaction object without authentication.
        """
        data = {'tx_type': '+', 'amount': 500}
        response = self.client.post(TransactionViewTests.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_tx_201(self):
        """
        Ensure we can create transaction object with authentication.
        """
        data = {'tx_type': '+', 'amount': 500}
        user = User.objects.get(username=TransactionViewTests.user)
        self.client.force_authenticate(user=user)
        response = self.client.post(TransactionViewTests.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().tx_type, '+')

    def test_list_tx_201(self):
        """
        Ensure we can list transaction objects via API with authentication.
        """
        user = User.objects.get(username=TransactionViewTests.user)
        self.client.force_authenticate(user=user)
        data = {'tx_type': '+', 'amount': 500}
        response = self.client.post(TransactionViewTests.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().tx_type, '+')
        response = self.client.get(TransactionViewTests.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['amount'], 500)

    def test_list_tx_401(self):
        """
        Ensure can't list transaction object without authentication.
        """
        data = {'tx_type': '+', 'amount': 500}
        response = self.client.get(TransactionViewTests.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BalanceViewTests(APITestCase):
    user = 'test'
    password = 'test123'
    url = reverse('ledger_book:balance')
    url_tx = reverse('ledger_book:tx')

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username=BalanceViewTests.user, password=BalanceViewTests.password)
        Transaction.objects.create(tx_type='+', amount=5000)

    def test_list_balance(self):
        """
        Ensure we can list balance object.
        """
        response = self.client.get(BalanceViewTests.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['amount'], 5000)

    def test_add_balance(self):
        """
        Ensure balance is added after transaction.
        """
        url = reverse('ledger_book:tx')
        data = {'tx_type': '+', 'amount': 1000}
        user = User.objects.get(username=BalanceViewTests.user)
        self.client.force_authenticate(user=user)
        time.sleep(1)
        response = self.client.post(BalanceViewTests.url_tx, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(BalanceViewTests.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Balance.objects.count(), 2)
        self.assertEqual(Balance.objects.latest('created').amount, 6000)

    def test_subtract_balance(self):
        """
        Ensure balance is subtracted after transaction.
        """
        time.sleep(1)
        Transaction.objects.create(tx_type='-', amount=2000)
        data = {'tx_type': '-', 'amount': 1000}
        user = User.objects.get(username=BalanceViewTests.user)
        self.client.force_authenticate(user=user)
        time.sleep(1)
        response = self.client.post(BalanceViewTests.url_tx, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(BalanceViewTests.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Balance.objects.count(), 3)
        self.assertEqual(Balance.objects.latest('created').amount, 2000)
