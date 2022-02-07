from django.db import models

from utility.validators import validate_typed_foreign_key
from .customerAccount import CustomerAccount


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, CustomerAccount, CustomerAccount.REGULAR)


class RegularAccount(models.Model):
    regular_acc_id = models.ForeignKey(CustomerAccount, primary_key=True, on_delete=models.CASCADE,
                                       validators=[validate_id])
