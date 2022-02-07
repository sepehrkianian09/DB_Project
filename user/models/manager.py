from django.db import models

from user.models.Employee import Employee


class Manager(models.Model):
    manager_id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    # bank_account_id = models.ForeignKey(BankAccount, unique=True)
