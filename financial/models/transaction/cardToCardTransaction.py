from django.core.exceptions import ValidationError
from django.db import models
from utility.validators import typed_foreign_key_validator_func
from .transaction import Transaction
from account.models import Account


class CardToCardTransaction(models.Model):
    card_to_card_transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE, primarykey=True, validators=[
        typed_foreign_key_validator_func(Transaction, Transaction.CARD_TO_CARD)
    ])
    src = models.ForeignKey(Account, on_delete=models.CASCADE)
    dst = models.ForeignKey(Account, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.src != self.dst:
            raise ValidationError("src, dst shouldn't be equal")
