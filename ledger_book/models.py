from django.db import models

# Create your models here.


class Source(models.Model):
    """
    Source of income/Expense
    """
    created = models.DateTimeField(
        verbose_name="Creation Time",
        auto_now_add=True, null=False)

    name = models.CharField(max_length=100, verbose_name="Name")

    class Meta:
        ordering = ('created', 'name')


class Transaction(models.Model):
    """
    Save each donation/expense transaction
    """
    TRANS_TYPE = (
        ('+', 'Income'),
        ('-', 'Expense')
    )

    tx_id = models.AutoField(
        primary_key=True,
        verbose_name="Transaction Id"
    )

    created = models.DateTimeField(
        verbose_name="Creation Time",
        auto_now_add=True, null=False)

    tx_type = models.CharField(
        choices=TRANS_TYPE,
        default='+',
        verbose_name="Transaction Type",
        )

    from_or_to = models.ForeignKey(
        Source,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Source"
    )

    amount = models.IntegerField(
        verbose_name="Amount",
        null=False
    )

    description = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Transaction Description'
    )

    class Meta:
        ordering = ('created', 'tx_type', 'amount', 'from_or_to')


class Balance(models.Model):
    """
    Save the Total Amount on per month basis
    """
    created = models.DateField(
        verbose_name="Creation Date",
        unique_for_month=True,
        auto_now_add=True, null=False)

    amount = models.IntegerField(
        verbose_name="Total Balance",
        null=False
    )

    def credit(self, amount):
        """
        Add to balance
        :param amount: amount to be added
        :return: nothing
        """
        pass

    def debit(self, amount):
        """
        deduct from balance
        :param amount: amount to be deducted
        :return: nothing
        """
        pass

    class Meta:
        ordering = ('created')
