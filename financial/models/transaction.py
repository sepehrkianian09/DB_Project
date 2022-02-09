from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from account.models import Account


class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField(auto_now_add=True, editable=False)

    applied = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CardToCardTransaction(Transaction):
    src = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='%(class)s_src')
    dst = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='%(class)s_dst')

    def clean(self):
        super().clean()
        if self.src == self.dst:
            raise ValidationError("src, dst shouldn't be equal")

        if not self.applied:
            src_account = Account.objects.get(pk=self.src)
            if src_account.balance - self.amount < 0:
                raise ValidationError("src doesn't have enough money")
            src_account.balance -= self.amount
            src_account.save()
            self.applied = True


class DepositWithDrawTransaction(Transaction):
    pass
