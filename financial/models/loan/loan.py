from django.core.exceptions import ValidationError
from django.db import models

from .loanType import LoanType
from account.models.customerAccount import regularAccount
from account.models import bankAccount

from datetime import datetime


def check_if_is_future(start_date):
    if start_date < datetime.now():
        raise ValidationError(f"start_date must be later than now")


class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type_id = models.ForeignKey(LoanType, on_delete=models.CASCADE)
    regular_acc_id = models.ForeignKey(regularAccount, on_delete=models.CASCADE)
    bank_acc_id = models.ForeignKey(bankAccount, on_delete=models.CASCADE)

    start_date = models.DateTimeField(
        validators=[
            check_if_is_future
        ]
    )
