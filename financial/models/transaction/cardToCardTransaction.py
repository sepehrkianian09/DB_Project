from django.core.exceptions import ValidationError
from django.db import models
from utility.validators import validate_typed_foreign_key
from .transaction import Transaction
from account.models import Account


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, Transaction, Transaction.CARD_TO_CARD)


class CardToCardTransaction(models.Model):
    card_to_card_transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE, primarykey=True,
                                                    validators=[validate_id])
    src = models.ForeignKey(Account, on_delete=models.CASCADE)
    dst = models.ForeignKey(Account, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.src != self.dst:
            raise ValidationError("src, dst shouldn't be equal")
