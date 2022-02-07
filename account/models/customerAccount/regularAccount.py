from django.db import models

from utility.validators import typed_foreign_key_validator_func
from .customerAccount import CustomerAccount


class RegularAccount(models.Model):
    regular_acc_id = models.ForeignKey(CustomerAccount, primarykey=True, on_delete=models.CASCADE, validators=[
        typed_foreign_key_validator_func(CustomerAccount, CustomerAccount.REGULAR)
    ])
