from django.db import models

from account.models.customerAccount import customerAccount


class RegularAccount(models.Model):
    regular_acc_id = models.ForeignKey(customerAccount, primarykey=True, on_delete=models.CASCADE)
