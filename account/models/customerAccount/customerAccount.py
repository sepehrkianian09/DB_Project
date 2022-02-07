from django.db import models
from account.models import Account
from user.models import Customer
from utility.validators import typed_foreign_key_validator_func


class CustomerAccount(models.Model):
    customer_acc_id = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=True, validators=[
        typed_foreign_key_validator_func(Account, Account.CUSTOMER)
    ])
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    REGULAR = 'R'
    PROFITING = 'P'
    CUSTOMER_ACC_TYPE_CHOICES = ((PROFITING, 'profiting'), (REGULAR, 'regular'))
    type = models.CharField(
        max_length=1,
        choices=CUSTOMER_ACC_TYPE_CHOICES,
        default=REGULAR
    )
