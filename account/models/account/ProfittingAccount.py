from django.db import models
from user.models import Manager


from account.models.account import CustomerAccount
from account.models.account import BankAccount
from  account.models.account import ProfittingType

class ProfittingAccount(models.Model):
    profiting_acc_id=models.ForeignKey(CustomerAccount, primarykey=True, on_delete=models.CASCADE())
    prof_type_id = models.ForeignKey(ProfittingType, on_delete=models.CASCADE())
    prof_bank_acc_id = models.ForeignKey(BankAccount, on_delete=models.CASCADE())
    profiting_start_date = models.DateTimeField(
        validators=[
            #     date<now
            # >account_creation_Date
        ]
    )
