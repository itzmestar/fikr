from django.test import TransactionTestCase, TestCase
from ledger_book.models import Balance, Transaction
from datetime import datetime
import time

# model's tests


class TransactionTest(TestCase):
    """
    Tests for Transaction Model
    """
    def create_tx(self, tx_type="+", amount=500, description="Testing Tx"):
        return Transaction.objects.create(tx_type=tx_type, amount=amount, description=description)

    def test_Transaction_creation(self):
        w = self.create_tx()
        self.assertTrue(isinstance(w, Transaction))
        self.assertEqual(w.tx_type, "+")
        self.assertEqual(w.amount, 500)
        self.assertEqual(w.description, "Testing Tx")
        self.assertEqual(Transaction.objects.count(), 1)


class BalanceTest(TestCase):
    """
    Tests for Balance Model
    """
    def setUp(self):
        self.create_tx()

    def create_tx(self, tx_type="+", amount=4000, description="Testing Tx"):
        Transaction.objects.create(created=datetime.now(), tx_type=tx_type, amount=amount, description=description)

    def test_Balance_decrement(self):
        amount = Balance.objects.latest('created').amount
        #print(amount, Balance.objects.count(), Balance.objects.all())
        time.sleep(1)
        self.create_tx(tx_type="-", amount=1500, description="Testing decrement")
        self.assertEqual(Balance.objects.count(), 2)
        #print(amount, Balance.objects.count(), Balance.objects.all())
        self.assertEqual(Balance.objects.latest('created').amount, amount-1500)

    def test_Balance_increment(self):
        amount = Balance.objects.latest('created').amount
        #print(amount, Balance.objects.count(), Balance.objects.all())
        time.sleep(1)
        self.create_tx(tx_type="+", amount=500, description="Testing increment")
        self.assertEqual(Balance.objects.count(), 2)
        #print(amount, Balance.objects.count(), Balance.objects.all())
        self.assertEqual(Balance.objects.latest('created').amount, amount + 500)
