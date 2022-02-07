from django.core.validators import
from  django.db import models
from user.models.Acount import Account
from user.models.Human import Customer
class CustomerAccount(models.Model):
    customer_acc_id= models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    customer_id=models.ForeignKey(Customer)
    NORMAL = 'N'
    PROFITTING = 'P'
    CUSTOMER_ACC_TYPE_CHOICES = ((PROFITTING, 'profiting'), (NORMAL, 'normal'))
    type = models.CharField(
        max_length=1,
        choices=CUSTOMER_ACC_TYPE_CHOICES,
        default=NORMAL
    )