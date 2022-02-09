from django.core.exceptions import ValidationError
from django.db import models

from account.models import BankAccount, RegularAccount
from .loanProfit import LoanProfit
from ..types.loanType import LoanType

from datetime import datetime

from ... import CardToCardTransaction


def check_if_is_future(start_date):
    if start_date < datetime.now():
        raise ValidationError(f"start_date must be later than now")


class Loan(LoanProfit):
    id = models.AutoField(primary_key=True)
    type_class = LoanType
    type_id = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    bank_acc_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

    start_date = models.DateTimeField(
        validators=[
            check_if_is_future
        ]
    )

    regular_acc_id = models.ForeignKey(RegularAccount, on_delete=models.CASCADE)

    loan_deposit_transaction = models.ForeignKey(CardToCardTransaction, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        c2c_transaction = CardToCardTransaction.objects.get(pk=self.card_to_card_transaction_id)

        if c2c_transaction.src != self.bank_acc_id:
            raise ValidationError("loan_deposit_transaction is not valid. src != bank_acc_id")
        if c2c_transaction.dst != self.regular_acc_id:
            raise ValidationError("loan_deposit_transaction is not valid. dst != regular_acc_id")

        loan_type = LoanType.objects.get(pk=self.type_id)
        if abs(c2c_transaction.amount - loan_type.amount) > 0.1:
            raise ValidationError("loan_deposit_transaction amount is not valid.")
