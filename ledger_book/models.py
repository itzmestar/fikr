from django.db import models

# Create your models here.
class Transaction(models.Model):
    """
    Save each donation/expense transaction
    """
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
