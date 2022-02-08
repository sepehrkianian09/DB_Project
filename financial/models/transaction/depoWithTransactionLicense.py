from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models

from .transaction import Transaction
from .depositWithDrawTransaction import DepositWithDrawTransaction
from user.models import Employee
from account.models import CustomerAccount


class DepoWithTransactionLicense(models.Model):
    transaction_id = models.AutoField(primary_key=True)

    depo_with_transaction_id = models.ForeignKey(DepositWithDrawTransaction, on_delete=models.CASCADE, unique=True,
                                                 null=True, blank=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer_acc_id = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)

    DEPOSIT = 'D'
    WITHDRAW = 'W'
    TRANS_TYPE_CHOICES = ((DEPOSIT, 'deposit'), (WITHDRAW, 'withdraw'))
    type = models.CharField(
        max_length=1,
        choices=TRANS_TYPE_CHOICES,
        default=DEPOSIT
    )

    transaction_limit = models.IntegerField(
        validators=[
            MaxValueValidator(3000000)
        ]
    )

    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    expiration_date = models.DateTimeField()

    def clean(self):
        super().clean()
        if self.expiration_date <= self.creation_date:
            raise ValidationError("expiration_date is not valid")

        if self.transaction_id is not None:
            depowith_transaction = DepositWithDrawTransaction.objects.get(pk=self.transaction_id)
            transaction = Transaction.objects.get(pk=depowith_transaction.depo_with_transaction_id)

            if transaction.amount > self.transaction_limit:
                raise ValidationError("Transaction has reached amount limit")
            if transaction.date > self.expiration_date:
                raise ValidationError("Transaction has executed later than Expiration Date")
