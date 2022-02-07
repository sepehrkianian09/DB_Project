from django.db import models
from financial.models.transaction import transaction, Transaction
from utility.validators import validate_typed_foreign_key


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, Transaction, Transaction.DEPO_WITH)


class DepositWithDrawTransaction(models.Model):
    depo_with_transaction_id = models.ForeignKey(transaction, on_delete=models.CASCADE, primarykey=True,
                                                 validators=[validate_id])
