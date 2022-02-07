from django.db import models
from financial.transaction import Transaction


class DepositWithDrawTransaction(models.Model):

    depo_width_transaction_id = models.ForeignKey(Transaction, primarykey=True, on_delete=models.CASCADE())
