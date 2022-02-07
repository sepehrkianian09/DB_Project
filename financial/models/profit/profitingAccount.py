from django.db import models

from account.models.customerAccount import customerAccount
from financial.models.profit import profitingType
from account.models import bankAccount
from utility.validators import validate_typed_foreign_key
from account.models.customerAccount import CustomerAccount


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, CustomerAccount, CustomerAccount.PROFITING)


class ProfitingAccount(models.Model):
    profiting_acc_id = models.ForeignKey(customerAccount, on_delete=models.CASCADE, primarykey=True, validators=[
        validate_id()
    ])
    prof_type_id = models.ForeignKey(profitingType, on_delete=models.CASCADE)
    prof_bank_acc_id = models.ForeignKey(bankAccount, on_delete=models.CASCADE)
    profiting_start_date = models.DateTimeField(auto_now_add=True, editable=False)

#     on Save, create ProfitPayments for this.
