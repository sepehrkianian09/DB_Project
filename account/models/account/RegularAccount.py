from django.db import models
from user.models import Manager


from account.models.account import CustomerAccount

class RegularAccount(models.Model):
    regular_acc_id=models.ForeignKey(CustomerAccount, primarykey=True, on_delete=models.CASCADE())
