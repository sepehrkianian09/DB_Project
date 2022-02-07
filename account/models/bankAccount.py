from django.db import models
from user.models import Manager
from utility.validators import typed_foreign_key_validator_func

from .account import Account


class BankAccount(models.Model):
    bank_acc_id = models.ForeignKey(Account, on_delete=models.CASCADE, primarykey=True, validators=[
        typed_foreign_key_validator_func(Account, Account.MANAGER)
    ])
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, unique=True)
