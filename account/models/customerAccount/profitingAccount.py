from django.db import models

from account.models.customerAccount import customerAccount
from account.models import bankAccount
from utility.validators import typed_foreign_key_validator_func
from .customerAccount import CustomerAccount
from financial.models.loan import profitingType


class ProfitingAccount(models.Model):
    profiting_acc_id = models.ForeignKey(customerAccount, on_delete=models.CASCADE, primarykey=True, validators=[
        typed_foreign_key_validator_func(CustomerAccount, CustomerAccount.PROFITING)
    ])
    prof_type_id = models.ForeignKey(profitingType, on_delete=models.CASCADE)
    prof_bank_acc_id = models.ForeignKey(bankAccount, on_delete=models.CASCADE)
    profiting_start_date = models.DateTimeField(auto_now_add=True, editable=False)

#     on Save, create ProfitPayments for this.
