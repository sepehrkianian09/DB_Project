from django.db import models

from .loanProfit import LoanProfit
from ..types import ProfitingType
from account.models import BankAccount
from utility.validators import validate_typed_foreign_key
from account.models import CustomerAccount


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, CustomerAccount, CustomerAccount.PROFITING)


class ProfitingAccount(LoanProfit):
    id = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE, primary_key=True, validators=[
        validate_id
    ])
    type_class = ProfitingType
    type_id = models.ForeignKey(ProfitingType, on_delete=models.CASCADE)
    bank_acc_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True, editable=False)

#     on Save, create ProfitPayments for this.
