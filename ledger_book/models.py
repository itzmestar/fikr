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
        ordering = ('created',)


class Transaction(models.Model):
    """
    Save each donation/expense transaction
    """
    TRANS_TYPE = (
        ('+', 'Income'),
        ('-', 'Expense')
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
        ordering = ('created',)


class Balance(models.Model):
    """
    Save the Total Amount on per month basis
    """
    created = models.DateTimeField(
        verbose_name="Creation Date",
        unique_for_month=True,
        auto_now_add=True, null=False)

    amount = models.IntegerField(
        verbose_name="Total Balance",
        null=False
    )
