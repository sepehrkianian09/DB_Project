from django.db import models
from account.models.loan import Loan
from account.models.transaction import Transaction

class DepositWithDrawTransaction(models.Model):

    depo_width_transaction_id = models.ForeignKey(Transaction, primarykey=True, on_delete=models.CASCADE())
