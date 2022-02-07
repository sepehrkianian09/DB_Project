from django.db import models

from account.models.customerAccount import customerAccount
from account.models import bankAccount
from financial.models.loan import profitingType


class ProfitingAccount(models.Model):
    profiting_acc_id = models.ForeignKey(customerAccount, on_delete=models.CASCADE, primarykey=True)
    prof_type_id = models.ForeignKey(profitingType, on_delete=models.CASCADE)
    prof_bank_acc_id = models.ForeignKey(bankAccount, on_delete=models.CASCADE)
    profiting_start_date = models.DateTimeField(
        auto_now_add=True,
    )

#     on Save, create ProfitPayments for this.
