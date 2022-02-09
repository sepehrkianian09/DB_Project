from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from account.models import Account, CustomerAccount
from .loan_and_profit import ProfitingAccount, ProfitingType, ProfitPayment
from datetime import date


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
            src_account.balance -= self.amount
            src_account.save()
            # if src_account.balance - self.amount < 0:
            #     raise ValidationError("src doesn't have enough money")
            if src_account.type == Account.CUSTOMER:
                src_customer_account = CustomerAccount.objects.get(pk=self.src)
                if src_customer_account.type == CustomerAccount.PROFITING:
                    src_profiting_account = ProfitingAccount.objects.get(pk=self.src)
                    src_profiting_type = ProfitingType.objects.get(pk=src_profiting_account.type_id)
                    payment_index = (date.today() - src_profiting_account.start_date).days / (
                            30 * src_profiting_type.payment_duration)
                    payment = ProfitPayment.objects.get(loan_profit_id=self.src, payment_index=payment_index)
                    payment.duration_withdrawal += self.amount
                    payment.save()
            self.applied = True


class DepositWithDrawTransaction(Transaction):
    pass
