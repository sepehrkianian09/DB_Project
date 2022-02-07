from django.core.validators import
from  django.db import models
from account.models.account import Account
from user.models.Human import Customer
class CustomerAccount(models.Model):
    customer_acc_id=models.ForeignKey(Account, on_delete=models.CASCADE())
    customer_id=models.ForeignKey(Customer)
    NORMAL = 'N'
    PROFITTING = 'P'
    CUSTOMER_ACC_TYPE_CHOICES = ((PROFITTING, 'profiting'), (NORMAL, 'normal'))
    type = models.CharField(
        max_length=1,
        choices=CUSTOMER_ACC_TYPE_CHOICES,
        default=NORMAL
    )