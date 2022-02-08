from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from account.models import Account


class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class CardToCardTransaction(Transaction):
    src = models.ForeignKey(Account, on_delete=models.CASCADE)
    dst = models.ForeignKey(Account, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.src != self.dst:
            raise ValidationError("src, dst shouldn't be equal")


class DepositWithDrawTransaction(Transaction):
    pass
