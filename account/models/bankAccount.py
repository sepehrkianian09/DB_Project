from django.db import models

from user.models import Manager
from utility.validators import validate_typed_foreign_key

from .account import Account


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, Account, Account.MANAGER)


class BankAccount(models.Model):
    bank_acc_id = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=True, validators=[
        validate_id
    ])
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
