
from django.db import models
from user.models import Manager


from account.models.account import Account

class BankAccount(models.Model):
    bank_acc_id=models.ForeignKey(Account, primarykey=True, on_delete=models.CASCADE())
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE())
