from django.db import models
from financial.models.transaction import transaction, Transaction
from utility.validators import typed_foreign_key_validator_func


class DepositWithDrawTransaction(models.Model):
    depo_with_transaction_id = models.ForeignKey(transaction, on_delete=models.CASCADE, primarykey=True,
                                                 validators=[
                                                     typed_foreign_key_validator_func(Transaction,
                                                                                      Transaction.DEPO_WITH)
                                                 ])
