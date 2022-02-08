from django.core.exceptions import ValidationError
from django.db import models

from account.models import BankAccount, RegularAccount
from .loanProfit import LoanProfit
from ..types.loanType import LoanType

from datetime import datetime


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
