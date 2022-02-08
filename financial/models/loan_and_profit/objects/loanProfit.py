from django.db import models

from account.models import BankAccount


class LoanProfit(models.Model):
    id = None
    type_class = None
    type_id = None
    bank_acc_id = None
    start_date = None

    class Meta:
        abstract = True
