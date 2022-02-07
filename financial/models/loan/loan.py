from django.core.exceptions import ValidationError
from django.db import models

from .loanType import LoanType
from account.models.account import RegularAccount
from account.models.account import BankAccount

from datetime import datetime


def check_if_is_future(start_date):
    if start_date < datetime.now():
        raise ValidationError(f"start_date must be later than now")


class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type_id = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    regular_acc_id = models.ForeignKey(RegularAccount, on_delete=models.CASCADE)
    bank_acc_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

    start_date = models.DateTimeField(
        validators=[
            check_if_is_future
        ]
    )
