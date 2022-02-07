from django.db import models
from account.models import account
from user.models import Customer


class CustomerAccount(models.Model):
    customer_acc_id = models.ForeignKey(account, on_delete=models.CASCADE, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    REGULAR = 'R'
    PROFITING = 'P'
    CUSTOMER_ACC_TYPE_CHOICES = ((PROFITING, 'profiting'), (REGULAR, 'regular'))
    type = models.CharField(
        max_length=1,
        choices=CUSTOMER_ACC_TYPE_CHOICES,
        default=REGULAR
    )
