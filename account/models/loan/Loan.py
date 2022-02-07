from django.db import models

from account.models.loan import LoanType
from account.models.account import RegularAccount
from account.models.account import BankAccount

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type_id = models.ForeignKey(LoanType, on_delete=models.CASCADE())
    regular_acc_id = models.ForeignKey(RegularAccount, on_delete=models.CASCADE())
    bank_acc_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE())

    start_date = models.DateTimeField(
        validators=[
            #     date<now
            # >account_creation_Date
        ]
    )
