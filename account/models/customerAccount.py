from django.db import models
from account.models import Account
from user.models import Customer
from utility.validators import validate_typed_foreign_key


def validate_id(employee_id):
    return validate_typed_foreign_key(employee_id, Account, Account.CUSTOMER)


class CustomerAccount(models.Model):
    customer_acc_id = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=True, validators=[validate_id])
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    REGULAR = 'R'
    PROFITING = 'P'
    CUSTOMER_ACC_TYPE_CHOICES = ((PROFITING, 'profiting'), (REGULAR, 'regular'))
    type = models.CharField(
        max_length=1,
        choices=CUSTOMER_ACC_TYPE_CHOICES,
        default=REGULAR
    )


def validate_regular_account_id(employee_id):
    return validate_typed_foreign_key(employee_id, CustomerAccount, CustomerAccount.REGULAR)


class RegularAccount(models.Model):
    regular_acc_id = models.ForeignKey(CustomerAccount, primary_key=True, on_delete=models.CASCADE,
                                       validators=[validate_regular_account_id])
