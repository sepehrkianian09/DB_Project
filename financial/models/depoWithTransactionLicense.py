from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models

from .loan_and_profit import ProfitingAccount, ProfitingType, ProfitPayment
from .transaction import DepositWithDrawTransaction
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

        if self.depo_with_transaction_id is not None:
            depo_with_transaction = DepositWithDrawTransaction.objects.get(pk=self.depo_with_transaction_id)

            if depo_with_transaction.amount > self.transaction_limit:
                raise ValidationError("Transaction has reached amount limit")
            if depo_with_transaction.date > self.expiration_date:
                raise ValidationError("Transaction has executed later than Expiration Date")

            if depo_with_transaction.applied is None:
                src_account = CustomerAccount.objects.get(pk=self.customer_acc_id)

                # if src_account.balance - depo_with_transaction.amount < 0:
                #     raise ValidationError("src doesn't have enough money")
                src_account.balance -= depo_with_transaction.amount
                src_account.save()
                if src_account.type == CustomerAccount.PROFITING:
                    src_profiting_account = ProfitingAccount.objects.get(pk=self.customer_acc_id)
                    src_profiting_type = ProfitingType.objects.get(pk=src_profiting_account.type_id)
                    payment_index = (date.today() - src_profiting_account.start_date).days / (
                            30 * src_profiting_type.payment_duration)
                    payment = ProfitPayment.objects.get(loan_profit_id=self.customer_acc_id,
                                                        payment_index=payment_index)
                    payment.duration_withdrawal += depo_with_transaction.amount
                    payment.save()

                depo_with_transaction.applied = True
                depo_with_transaction.save()
