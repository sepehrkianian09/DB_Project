from django.core.validators import
from django.db import models
from user.models import Manager


class BankAccount(models.Model):
    bank_acc_id=models.AutoField(primarykey=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE())
